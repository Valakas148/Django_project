import re


class LanguageBadCheckService:
    @staticmethod
    def check_language_bad(text):
        bad_words = [
            r'\bсука\b', r'\bбля\b', r'\bблядь\b', r'\bпідар\b', r'\bхуй\b', r'\bпизда\b', r'\bєбать\b',
            r'\bshit\b', r'\bfuck\b', r'\basshole\b', r'\bbitch\b', r'\bcunt\b', r'\bdick\b', r'\bpussy\b',
            r'\bmotherfucker\b', r'\bcock\b', r'\bdouche\b'
        ]
        pattern = re.compile(r'|'.join(bad_words), re.IGNORECASE)

        if pattern.search(text):
            return True
        return False