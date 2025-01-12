def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts[0], parts[1], parts[2]

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(num1), len(num2)) + 2
        top_line = num1.rjust(max_length)
        bottom_line = operator + num2.rjust(max_length - 1)
        line = "-" * max_length

        if show_answers:
            if operator == "+":
                result = str(int(num1) + int(num2)).rjust(max_length)
            else:
                result = str(int(num1) - int(num2)).rjust(max_length)
            arranged_problems["result"].append(result)

        arranged_problems["top"].append(top_line)
        arranged_problems["bottom"].append(bottom_line)
        arranged_problems["line"].append(line)

    top_row = "    ".join(arranged_problems["top"])
    bottom_row = "    ".join(arranged_problems["bottom"])
    line_row = "    ".join(arranged_problems["line"])
    result_row = "    ".join(arranged_problems["result"])

    if show_answers:
        return f"{top_row}\n{bottom_row}\n{line_row}\n{result_row}"
    else:
        return f"{top_row}\n{bottom_row}\n{line_row}"
#Puedes usar esta función para resolver problemas aritméticos y mostrarlos en formato vertical. Aquí tienes un ejemplo de cómo llamar a la función:

# python
# Copy code


problems_with_answers =["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems_with_answers, True))
# Esto mostrará los problemas aritméticos ordenados verticalmente, como se muestra en tu ejemplo.






