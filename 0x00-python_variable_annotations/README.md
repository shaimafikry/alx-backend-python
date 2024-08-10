# Type annotations in Python 3
Type annotations in Python were introduced to provide a way to specify the expected types of variables and function signatures, making code more readable and reducing runtime errors. Here's a breakdown of the key concepts:

### 1. Type Annotations in Python 3
Type annotations allow you to specify the expected types for function arguments, return values, and variables. These annotations are not enforced at runtime but can be used by tools like `mypy` to check for type consistency.

#### Function Signatures
You can annotate the types of a function’s arguments and its return value:

```python
def add(x: int, y: int) -> int:
    return x + y
```

In this example:
- `x: int` means `x` is expected to be of type `int`.
- `y: int` means `y` is expected to be of type `int`.
- `-> int` indicates that the function returns an `int`.

#### Variable Annotations
Variables can also be annotated with types:

```python
age: int = 25
name: str = "John"
```

### 2. Duck Typing
Duck typing is a concept in Python where the type or class of an object is less important than the methods it defines or the operations it supports. The name comes from the saying, "If it looks like a duck and quacks like a duck, it’s probably a duck."

Instead of checking if an object is an instance of a particular class, Python relies on whether the object supports the required operations (methods, properties, etc.).

Example:

```python
class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_it_quack(duck: Duck):
    duck.quack()

d = Dog()
make_it_quack(d)  # Works because Dog has a quack method
```

Here, even though `d` is an instance of `Dog`, it works with the `make_it_quack` function because `Dog` has a `quack` method.

### 3. Validating Your Code with `mypy`
`mypy` is a static type checker for Python. It reads your type annotations and checks whether your code is type-safe.

To use `mypy`, you should install it first:

```bash
pip install mypy
```

Then, you can run it on your code:

```bash
mypy your_script.py
```

If there are type inconsistencies, `mypy` will report them. For example:

```python
def greet(name: str) -> int:
    return f"Hello, {name}"

# Running mypy will flag this:
# error: Incompatible return value type (got "str", expected "int")
```

In this example, `mypy` will flag an error because the function is expected to return an `int`, but it actually returns a `str`.

### Summary
- **Type Annotations**: Allow you to specify the expected types for function arguments, return values, and variables.
- **Duck Typing**: Emphasizes what an object can do over its type.
- **Validating with `mypy`**: Helps catch type errors in your code by checking against the specified annotations.

These tools and concepts help improve code quality, readability, and maintainability.

_________________________________________________

The expression `annotations = safely_get_value.__annotations__` is used to retrieve the type annotations for a function or method in Python. Here's a detailed explanation:

### 1. Understanding the Code
- **`safely_get_value`**: This is the name of a function (or method) defined somewhere in your code.
- **`.__annotations__`**: This is a special attribute in Python that holds a dictionary of type annotations for the function's parameters and return type.

### 2. What `.__annotations__` Contains
When you annotate a function's parameters and return type, Python stores these annotations in the function's `__annotations__` attribute as a dictionary. The keys in this dictionary are the names of the parameters, and the values are the types you’ve specified. The return type is stored with the key `'return'`.

#### Example

Let's say you have the following function:

```python
def safely_get_value(data: dict, key: str, default: int = 0) -> int:
    return data.get(key, default)
```

The `__annotations__` attribute for `safely_get_value` would look like this:

```python
{
    'data': dict,
    'key': str,
    'default': int,
    'return': int
}
```

### 3. Assigning `annotations`
When you write:

```python
annotations = safely_get_value.__annotations__
```

You are assigning the dictionary containing the function's type annotations to the variable `annotations`. This allows you to inspect or use the annotations elsewhere in your code.

### 4. Use Cases
Inspecting the `__annotations__` can be useful in various scenarios, such as:
- **Documentation**: Automatically generating documentation that includes type information.
- **Validation**: Creating custom validation logic based on expected types.
- **Introspection**: Writing tools or libraries that need to understand the types used in functions.

### Example in Action

```python
def safely_get_value(data: dict, key: str, default: int = 0) -> int:
    return data.get(key, default)

annotations = safely_get_value.__annotations__
print(annotations)
```

Output:

```python
{'data': dict, 'key': str, 'default': int, 'return': int}
```

This dictionary output shows the type annotations for each parameter and the return type of the `safely_get_value` function.

### Summary
- **`__annotations__`** is a dictionary attribute that stores the type annotations for a function’s parameters and return type.
- By assigning `safely_get_value.__annotations__` to a variable like `annotations`, you can inspect and use these type annotations programmatically.
