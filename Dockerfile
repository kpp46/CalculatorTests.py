FROM Python:3

ADD src /src

CMD["python", ".src/CalculatorTests.py"]
