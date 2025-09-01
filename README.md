# Music Playlist API
A RESTful API built with **Django** and **Django REST Framework** to manage users, artists, albums, songs, playlists and genres.
## Quick start

**Clone repository & install dependencies**

```bash
git clone <your-repo-url>
cd <repo-folder>
python -m venv venv
source venv/bin/activate   # macOS / Linux
# On Windows: run venv/Scripts/activate
pip install -r requirements.txt
```

**Database and run**

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# Open http://127.0.0.1:8000/
```

---

## Tech stack

* Python 3.10+
* Django
* Django REST Framework (DRF)
* djangorestframework-simplejwt (JWT authentication)

---

## API endpoints (summary)

All API endpoints are prefixed with `/api/`.

```text
GET/POST    /api/users/                       -> GET is used to fetch detaiils about each user, you must be authenticated to perform this action
GET         /api/users/<int:pk>/              -> This is used to fetch details about a specific user based on their id. Authorization is for authenticated users only
GET/POST    /api/artists/                     -> Any authenticated user can create a new artist
GET/PUT/DEL /api/artists/<int:pk>/            -> PUT/ DEL Operation scan only be performed by the owner/creator of that artist
GET/POST    /api/albums/                      -> GET operation provides details on every album created. POST operation is for creating a new album. Authorization is Authenticated users only
GET/PUT/DEL /api/albums/<int:pk>/             -> PUT/DEL operations can only be performed by the owenr/creator of the album
GET/POST    /api/songs/                       -> GET operation provides details on every song created. POST operation is for creating a new song. Authorization is Authenticated users only
GET/PUT/DEL /api/songs/<int:pk>/              -> PUT/DEL operations can only be performed by the owner/creator of the song
GET/POST    /api/playlists/                   -> GET operation fetches detail on every playlist created. POST operation is for creating a new playlist
GET/PUT/DEL /api/playlists/<int:pk>/          -> PUT/DEL operations can only be performed by the owner/creator of the playlist
POST/DELETE /api/playlists/<int:pk>/songs/    -> POST operation is for adding a song to a playlist (including the order), while DELETE operation is for removing a song from a playlist. AUthorization here is for the owner only
GET         /api/genres/                      -> This is for listing all available genres. Authorization is for authenticated users
POST        /api/genres/create/               -> This is for creating a new genre, Authorization here is admin only
POST        /api/register/                    -> This operation is for registering a new user (with a username, email and password)
POST        /api/token/                       -> This is for obtaining your access and refresh token (Provide credentials)
POST        /api/token/refresh/               -> This is for retrieveing a new access token, in case yours has already expired (You'll need to provide your refresh token)
```

---

## Authentication

* **Register**: `POST /api/register/` — create a new user (open to public)
* **Obtain token**: `POST /api/token/` — returns `access` and `refresh` JWT tokens
* **Refresh token**: `POST /api/token/refresh/`

For all protected endpoints include the `Authorization` header:

```
Authorization: Bearer <ACCESS_TOKEN>
```

---

## Examples (curl)

### 1) Register a user

```bash
curl -X POST http://127.0.0.1:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"Michael","email":"michael@gmail.com","password":"strongpassword"}'
```

### 2) Obtain JWT tokens

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"michael","password":"strongpassword"}'
```

**Response** (example)

```json
{
  "refresh": "<REFRESH_TOKEN>",
  "access": "<ACCESS_TOKEN>"
}
```

### 3) Create an artist (authenticated)

```bash
curl -X POST http://127.0.0.1:8000/api/artists/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{"name":"Green day", "bio": "A rock band"}'
```

### 4) Add a song to a playlist

**Request example** 

```bash
curl -X POST http://127.0.0.1:8000/api/playlists/1/songs/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{"song_id": 2, "order": 1 }'
```

**Postman tip:**

* Use the *Headers* tab to add `Authorization: Bearer <ACCESS_TOKEN>` or choose Authorization ➜ Bearer Token.
* Also use the *Headers* tab to add `Content-Type: application/json`

## Examples (Postman)
*Registering a new account
```bash
POST https://manlikeobaro.pythonanywhere.com/api/register/
Content-Type: application/json
```
* body
```
      {
          "username": "User",
          "email": "user@gmail.com",
          "password": "userpassword"
      }
```
*response
```
      {
          "user": {
              "id": 10,
              "username": "User",
              "email": "user@gmail.com"
          },
                "access": <ACCESS_TOKEN>,
                "refresh": <REFRESH_TOKEN>
      }
```

*Logging in to get a token
```bash
POST https://manlikeobaro.pythonanywhere.com/api/token/
Content-Type: application/json
```
* body
```
      {
          "username": "User",
          "password": "userpassword"
      }
```
*response
```
      {
          "refresh": <REFRESH_TOKEN>,
          "access": <ACCESS_TOKEN>
      }
```

*Listing all artists
```bash
POST https://manlikeobaro.pythonanywhere.com/api/artists/
Content-Type: application/json
Authorization: Bearer <ACCESS_TOKEN>
```

*response
```
      [
            {
                "id": 1,
                "owner": {
                    "id": 1,
                    "username": "testuser",
                    "email": "testuser@gmail.com"
                },
                "name": "Eminem",
                "bio": "From Detroit, a legend"
            },
            ...
            ...
      ]
```

*Creating an artist
```bash
POST https://manlikeobaro.pythonanywhere.com/api/artists/
Content-Type: application/json
Authorization: Bearer <ACCESS_TOKEN>
```
* body
```
      {
          "name": "J.cole",
          "bio": "A good rapper"
      }
```
*response
```
      {
    "id": 11,
    "owner": {
        "id": 10,
        "username": "User",
        "email": "user@gmail.com"
    },
    "name": "J.cole",
    "bio": "A good rapper"
}
```

*Updating an artist
```bash
PUT https://manlikeobaro.pythonanywhere.com/api/artists/11/ (Note: Change the number to the id of the artist you created)
Content-Type: application/json
Authorization: Bearer <ACCESS_TOKEN>
```
* body
```
      {
          "name": "J.cole",
          "bio": "A decent rapper"
      }
```
*response
```
{
    "id": 11,
    "owner": {
        "id": 10,
        "username": "User",
        "email": "user@gmail.com"
    },
    "name": "J.cole",
    "bio": "A decent rapper"
}
```

*Deleting an artist
```bash
DELETE https://manlikeobaro.pythonanywhere.com/api/artists/11/ (Note: Change the number to the id of the artist you created)
Content-Type: application/json
Authorization: Bearer <ACCESS_TOKEN>
```
* No body request (since we've gotten the artist by id in the link)
*response
```
204 NO CONTENT
```
