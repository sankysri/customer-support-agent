# customer_support_agent/tools.py

def search_knowledge_base(query: str) -> str:
    mock_kb = {
        "reset password": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions.",
        "update email": "You can update your email in the 'Account Settings' page after logging in.",
        "refund policy": "Our refund policy allows for full refunds within 30 days of purchase. Contact support for more info."
    }

    for key, answer in mock_kb.items():
        if key in query.lower():
            return answer

    return "No relevant information found in the knowledge base."

def create_support_ticket(issue: str) -> str:
    print(f"[Ticket Created] Issue: {issue}")
    return "A support ticket has been created. Our team will get back to you shortly."
