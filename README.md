# Django Authentication API

A Django REST Framework-based authentication API that implements token-based authentication.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install django djangorestframework
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a test user:
```bash
python manage.py create_test_user
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Login
- **URL**: `/api/login/`
- **Method**: `POST`
- **Data Params**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Success Response**:
  - **Code**: 200
  - **Content**:
    ```json
    {
      "token": "your-auth-token"
    }
    ```
- **Error Response**:
  - **Code**: 400
  - **Content**:
    ```json
    {
      "non_field_errors": [
        "Invalid username or password."
      ]
    }
    ```

## Testing with cURL

```bash
# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

## Testing with Postman

1. Create a new POST request to `http://localhost:8000/api/login/`
2. Set the Content-Type header to `application/json`
3. In the request body, select "raw" and "JSON", then enter:
```json
{
    "username": "testuser",
    "password": "testpass123"
}
```
4. Send the request

## Using the Token

Once you have received a token, include it in the Authorization header for subsequent requests:

```bash
curl -H "Authorization: Token your-token-here" http://your-api-endpoint
```

In Postman:
1. Add a header
2. Key: `Authorization`
3. Value: `Token your-token-here` 