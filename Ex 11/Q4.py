# Q4) Password Strength Checker: Implement a Python function that checks the strength of a 
# given password based on predefined criteria using regular expressions. Criteria might 
# include minimum length, presence of uppercase letters, lowercase letters, digits, and 
# special characters.

import re

def check_password_strength(password):
    """
    Check password strength based on multiple criteria
    """
    score = 0
    feedback = []
    
    # Criteria checks
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate score
    if length_ok:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")
    
    if has_upper:
        score += 1
    else:
        feedback.append("❌ Password should contain at least one uppercase letter")
    
    if has_lower:
        score += 1
    else:
        feedback.append("❌ Password should contain at least one lowercase letter")
    
    if has_digit:
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit")
    
    if has_special:
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character")
    
    # Determine strength level
    if score == 5:
        strength = "💪 Very Strong"
    elif score == 4:
        strength = "👍 Strong"
    elif score == 3:
        strength = "⚠️  Moderate"
    elif score == 2:
        strength = "👎 Weak"
    else:
        strength = "❌ Very Weak"
    
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback,
        'length': len(password)
    }

def main():
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ").strip()
        
        if password.lower() == 'quit':
            print("👋 Goodbye!")
            break
        
        if not password:
            print("❌ Please enter a password!")
            continue
        
        result = check_password_strength(password)
        
        print(f"\n📊 Password Analysis:")
        print(f"   Length: {result['length']} characters")
        print(f"   Score: {result['score']}/5")
        print(f"   Strength: {result['strength']}")
        
        if result['feedback']:
            print(f"\n💡 Suggestions:")
            for suggestion in result['feedback']:
                print(f"   {suggestion}")
        else:
            print(f"\n✅ Excellent! Your password meets all criteria!")

if __name__ == "__main__":
    main()
