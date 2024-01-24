# Motivational Quote Sender

<p align="center">
  <img src="https://i.imgur.com/HyuGik4.jpg" alt="Motivational Quote Sender">
</p>



Welcome to the **Motivational Quote Sender** project! Elevate your Mondays with a burst of positivity through randomly generated motivational quotes delivered straight to your inbox. Let's embark on a journey of inspiration together.

## Prerequisites

Before we begin, ensure you have the following set up:

- **Python 3**
- **Active Gmail account**

## Installation

1. **Clone Repository:**

    ```bash
    git clone https://github.com/your-username/motivational-quote-sender.git
    ```

2. **Navigate to Project:**

    ```bash
    cd motivational-quote-sender
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Open the `motivational_quote_sender.py` file and personalize the following variables:

```python
my_email = "your@gmail.com"
password = "your_password"
receiver = "recipient@example.com"
day_to_send = 0  # Set to your preferred day (0 = Monday)
```

## Running the Script

Execute the script with:

```bash
python motivational_quote_sender.py
```

The script checks if today aligns with the specified day to deliver a motivational quote. If affirmative, a randomly selected quote from `quotes.txt` will be sent to the provided email address.

## Customization

Make this experience uniquely yours by modifying quotes in `quotes.txt` or experimenting with different email formats. Add more functionality to cater to your preferences and share the positivity.


Feel free to contribute, spreading motivation to others! For issues or suggestions, open an issue or submit a pull request. Let's code our way to a motivated life! 🌟
