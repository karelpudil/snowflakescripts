from datetime import datetime

def main(session): # Snowflake passes a session object her
  today = datetime.now()
  date_str = today.strftime("%d%b%Y")
  return f"Today is {date_str}"
