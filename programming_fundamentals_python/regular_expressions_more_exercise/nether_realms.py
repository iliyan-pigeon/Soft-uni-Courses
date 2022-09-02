import re

demons = sorted([demon.strip() for demon in input().split(", ")])
for demon in demons:
    health_pattern = r"[^\d\+\-\*\/\.\]"
    damage_pattern = r"\-?\d+\.?\d*"
    m_and_d_pattern = r"[\/\*]"
    health = sum([ord(ch) for ch in re.findall(health_pattern, demon)])
    damage = sum([float(ch) for ch in re.findall(damage_pattern, demon)])
    m_and_d = re.findall(m_and_d_pattern, demon)
    if m_and_d:
        for symbol in m_and_d:
            if symbol == '*':
                damage *= 2
            elif symbol == "/":
                damage /= 2
    print(f"{demon} - {health} health, {damage:.2f} damage")
