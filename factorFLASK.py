from flask import Flask, request

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/', methods=['GET', 'POST'])
def calculate_factorial():
    if request.method == 'POST':
        # Get the number from the form
        number = request.form.get('number')

        # Validate and calculate factorial
        if number:
            try:
                num = int(number)
                if num < 0:
                    return "Factorial is not defined for negative numbers."
                result = factorial(num)
                return f"Factorial of {num} is: {result}"
            except ValueError:
                return "Invalid input. Please enter a valid integer."
        else:
            return "Please enter a number."

    # HTML form for input
    return '''
        <h1>Factorial Calculator</h1>
        <form method="POST">
            Enter a number: <input type="text" name="number"><br><br>
            <input type="submit" value="Calculate">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)