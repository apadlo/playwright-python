# Playwright Python Test Suite

## Setup

### Environment Variables

This project uses environment variables to manage sensitive credentials securely. 

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Fill in your actual credentials in the `.env` file:
   ```
   USER_PASSWORD=your_actual_password
   TEST_EMAIL=your_test_email@example.com
   PRACTICE_USERNAME=rahulshettyacademy
   PRACTICE_PASSWORD=your_practice_password
   PRACTICE_WRONG_PASSWORD=test_wrong_password
   ```

3. **Important**: Never commit the `.env` file to version control. It is already listed in `.gitignore`.

### Installation

```bash
pip install -r requirements.txt
```

### Running Tests

```bash
pytest
```

## Security

All sensitive data such as passwords, API keys, and credentials are managed through environment variables. This ensures:
- Credentials are not hardcoded in the codebase
- Sensitive data is not committed to version control
- Each environment can use different credentials

If you find any hardcoded credentials, please report them immediately or submit a pull request to remove them.
