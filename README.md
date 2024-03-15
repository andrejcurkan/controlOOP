# Приложение калькулятора комплексных чисел на Python с использованием архитектурных паттернов и принципов SOLID.
структура проекта:
| Директория         | Файлы                      |
|--------------------|----------------------------|
| calculator_project |                            |
| complex_numbers    | __init__.py, complex_number.py, complex_number_factory.py |
| calculator         | __init__.py, calculator.py |
| input_validation   | __init__.py, input_validation.py |
| logging_utils      | __init__.py, logger.py     |
| operations         | __init__.py, operations.py |
| user_interaction   | __init__.py, user_interaction.py |
|                    | main.py                    |

│   └── user_interaction.py
│
└── main.py


   * complex_numbers: модули для работы с комплексными числами.
   * calculator: модуль для выполнения математических операций с комплексными числами.
   * input_validation: модуль для валидации ввода пользователя.
   * logging_utils: модуль для логирования.
   * operations: модуль, содержащий операции над комплексными числами.
   * user_interaction: модуль для взаимодействия с пользователем.
   * main.py: точка входа в приложение.
