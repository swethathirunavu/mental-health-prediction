def get_supportive_message(level):
    level = level.lower()
    
    if level == "low":
        return (
            "😊 You seem to be doing fine, but it's always good to take breaks, "
            "sleep well, and talk to friends or loved ones."
        )
    elif level == "moderate":
        return (
            "😌 You're under moderate pressure. Try activities like journaling, "
            "listening to calming music, or taking walks in nature."
        )
    elif level == "high":
        return (
            "😟 You're going through a tough time. Please consider talking to someone you trust, "
            "reach out to a counselor, and take care of your mental well-being. You’re not alone."
        )
    else:
        return "🤖 I'm here for you. Try to relax and take one step at a time. You matter!"
