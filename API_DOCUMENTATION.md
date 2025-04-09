# Career Opportunities Navigator API Documentation

## Introduction
This API powers the Career Opportunities Navigator application, providing endpoints for:
- User account management (registration, login)
- Resume creation and management
- Resume section management (personal info, education, experience, etc.)
- Resume processing (parsing, optimization, and export)

The API follows RESTful principles and returns JSON responses unless otherwise specified.

## Base URL
All endpoints are prefixed with: `/api/v1`

## Authentication
The API uses JWT (JSON Web Tokens) for authentication. Most endpoints require an Authorization header with a valid token.

To obtain a token:
1. Register a user account via `/users` endpoint
2. Login via `/login` endpoint to get your token
3. Include the token in subsequent requests as:
   `Authorization: Bearer {your_token}`

## User Management

### Register User
**Endpoint**: `POST /users`

**Description**: Creates a new user account. Email must be unique.

**Request Body**:
```json
{
  "name": "string",
  "email": "user@example.com",
  "password": "string"
}
```

**Response** (201 Created):
```json
{
  "id": "string",
  "name": "string",
  "email": "string",
  "created_at": "datetime"
}
```

**Errors**:
- 400: Invalid request data (missing fields or invalid email)
- 409: User with email already exists

### Login User
**Endpoint**: `POST /login`

**Description**: Authenticates user and returns JWT token

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "string"
}
```

**Response** (200 OK):
```json
{
  "access_token": "string",
  "token_type": "bearer",
  "user": {
    "id": "string",
    "name": "string",
    "email": "string"
  }
}
```

**Errors**:
- 400: Invalid request data
- 401: Invalid credentials

## Resume Management

### Create Resume
**Endpoint**: `POST /resumes`

**Description**: Creates a new resume for the authenticated user

**Request Body**:
```json
{
  "user_id": "string",
  "title": "string",
  "summary": "string",
  "section_settings": [
    {
      "name": "string",
      "visible": true,
      "order": 1
    }
  ]
}
```

**Response** (201 Created):
```json
{
  "id": "string",
  "user_id": "string",
  "title": "string",
  "summary": "string",
  "section_settings": [...],
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**Errors**:
- 400: Invalid request data
- 401: Unauthorized
- 404: User not found

[Additional sections would continue here with similar detail for all endpoints]
