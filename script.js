document.getElementById("year").textContent = new Date().getFullYear();

const collaborationGrid = document.querySelector("[data-collaborations]");
if (collaborationGrid) {
  fetch("../data/collaborations.json")
    .then((response) => {
      if (!response.ok) throw new Error("Collaboration data unavailable");
      return response.json();
    })
    .then((projects) => {
      if (!Array.isArray(projects) || !projects.length) return;
      const english = document.documentElement.lang === "en";
      collaborationGrid.replaceChildren();
      for (const project of projects) {
        const card = document.createElement("article");
        card.className = "content-card collaboration-card";
        if (project.image) {
          const image = document.createElement("img");
          image.src = project.image;
          image.alt = project.title;
          image.loading = "lazy";
          card.append(image);
        }
        const genre = document.createElement("span");
        genre.className = "status-pill";
        genre.textContent = [project.genre, project.bpm && `${project.bpm} BPM`].filter(Boolean).join(" · ");
        const title = document.createElement("h3");
        title.textContent = project.title;
        const artists = document.createElement("p");
        artists.className = "collaboration-artists";
        artists.textContent = project.artists;
        const summary = document.createElement("p");
        summary.textContent = english ? project.summaryEn : project.summaryFr;
        card.append(genre, title, artists, summary);
        if (project.listenUrl) {
          const link = document.createElement("a");
          link.className = "text-link";
          link.href = project.listenUrl;
          link.target = "_blank";
          link.rel = "noopener noreferrer";
          link.textContent = english ? "Listen to the project" : "Écouter le projet";
          card.append(link);
        }
        collaborationGrid.append(card);
      }
    })
    .catch(() => {});
}
