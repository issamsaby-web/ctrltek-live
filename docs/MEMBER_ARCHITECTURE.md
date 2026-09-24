# CTRLtek.Live — Member Account & Artist Profile Architecture

Status: P0 product specification
Date: 2026-09-24

## 1. Principle

One CTRLtek.Live account represents one person. A member can create an artist identity/profile used across Community, Collab, Creative Services, Records and Live.

Community registration is open and free. Membership tier must never determine A&R approval or booking selection.

## 2. Membership tiers

### Free
- Account
- Artist profile
- Artist directory / discovery
- Apply to open collaborations
- Remix contests
- Submit demos to CTRLtek.Live Records
- Live / booking eligibility
- Buy Creative Services

### Collective
- Everything in Free
- Full Collab Engine access
- Project workspaces
- Project chat
- Files / stems
- Version tracking
- Advanced feedback
- Knowledge Base / resources
- Preferential Creative Services pricing

Pricing validated for MVP:
- Founding Member: EUR 4.90/month for first 50 qualifying subscribers, retained while subscription remains continuously active
- Standard Collective: EUR 9.90/month

## 3. Account model

`Member`

Required:
- id
- email
- password/auth provider reference
- display_name
- preferred_language (`fr`, `en`)
- membership_tier (`free`, `collective`)
- membership_status (`active`, `past_due`, `cancelled`, `none`)
- created_at
- updated_at

Operational:
- onboarding_status
- email_verified_at
- last_login_at
- terms_accepted_at
- privacy_accepted_at
- marketing_consent (optional)

Do not expose private account fields publicly.

## 4. Artist profile model

`ArtistProfile`

Identity:
- id
- member_id
- slug
- artist_name
- short_bio
- full_bio
- avatar_url
- hero_image_url
- country
- city
- languages

Music:
- genres[]
- subgenres[]
- roles[] (`producer`, `dj`, `live_act`, `vocalist`, `musician`, `controllerist`, `other`)
- soundcloud_url
- spotify_url
- youtube_url
- bandcamp_url
- website_url
- instagram_url
- other_social_urls[]

Collaboration:
- open_to_collabs
- collaboration_interests[] (`originals`, `remix`, `vocals`, `mixing`, `live`, `other`)
- daw[]
- collaboration_notes

Live / booking:
- available_for_booking
- performance_types[] (`dj`, `live`, `hybrid`, `controllerism`)
- set_durations[]
- travel_regions[]
- booking_notes
- public_booking_contact_mode (platform-mediated by default)

Records:
- accepts_ar_contact
- demo_submission_enabled

System:
- profile_status (`draft`, `published`, `suspended`)
- completeness_score
- created_at
- updated_at

## 5. Public vs private

### Public profile
May expose:
- artist name
- avatar / hero image
- city + country (artist-controlled)
- bio
- genres / roles
- music links
- public social links
- collaboration availability
- performance types
- booking availability

### Private member data
Never expose by default:
- login email
- billing data
- legal identity
- private phone number
- private address
- contracts
- royalty/payment information
- private workspace files/messages
- A&R internal notes

## 6. Artist URL

Canonical public route:

`/artists/{slug}`

Examples:
- `/artists/issamfire`
- `/artists/spidy`

Slug rules:
- lowercase
- ASCII-friendly
- hyphen-separated
- unique
- reserved slugs blocked (`admin`, `api`, `records`, `live`, `services`, `collab`, etc.)

## 7. Onboarding

### Step 1 — Create free account
Minimum friction:
- email
- password / supported auth provider
- display name
- preferred language
- Terms + Privacy acceptance

### Step 2 — Create artist profile
- artist name
- primary role
- primary genre
- country
- short bio
- one music/social link

Profile can then be published.

### Step 3 — Progressive enrichment
Do not block registration on a large form. Prompt later for:
- additional links
- collaboration preferences
- DAW / workflow
- live capabilities
- booking availability
- full biography

## 8. Dashboard navigation

- Dashboard
- My Artist Profile
- Collabs
  - My Workspaces
  - Open Projects
  - Remix Contests
- Messages
- Files
- Creative Services
  - My Orders
  - Order a Service
- Records
  - My Demos
  - Submit Demo
  - Deals
  - Releases
  - Royalties
- Live
  - Opportunities
  - Applications
  - Bookings
- Knowledge Base
- Account & Billing

Not all sections need full implementation in P0. Navigation/data architecture should anticipate them without pretending unavailable features already work.

## 9. Permissions

Roles are separate from paid membership.

Platform roles:
- `member`
- `staff`
- `ar`
- `admin`

Future optional roles:
- `service_provider`
- `booking_manager`

Principles:
- Collective is a billing entitlement, not an administrative role.
- A&R users can access demo review data but not billing secrets.
- Service providers should only access assigned service workspaces.
- Project members only access workspaces they belong to.

## 10. MVP implementation boundary

P0/P1 must support:
1. Register / login / logout
2. Free account by default
3. Create/edit/publish artist profile
4. Public artist profile route
5. Artist directory
6. Membership entitlement field ready for Collective billing

Do not build yet:
- automated royalties
- internal full CRM
- Ableton Sync Agent
- complex recommendation engine
- mobile app

## 11. Security baseline

- Never store plaintext passwords.
- Use a mature authentication provider/library rather than custom cryptography.
- Server-side authorization for every private resource.
- Validate uploads and constrain file types/sizes.
- Rate-limit authentication and public forms.
- CSRF protection where relevant to chosen architecture.
- Secure session cookies when cookie sessions are used.
- Separate public profile data from private account/billing/legal data.
- Log privileged administrative actions.

## 12. Next technical decision

The repository is currently a static frontend. Before implementing authentication, choose the MVP application/backend architecture and hosting model.

The next engineering task is therefore: **select the authentication + database + billing stack and define the migration path from the current static site without breaking the public FR/EN pages.**
