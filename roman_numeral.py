def roman_to_int(numeral):
    final_answer = 0

    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV", "")


    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1

    return final_answer



while True:
    roman_input = input("Enter the Roman numeral you want to convert: ").upper()

    result = roman_to_int(roman_input)
    print(f"The Roman numeral {roman_input} translates to: {result}!")

    again = input("Do you want to convert another Roman numeral? (yes/no): ").lower()
    if again not in ("yes", "y"):
        print("👋 Exiting Roman Numeral Converter. Goodbye!")
        break
