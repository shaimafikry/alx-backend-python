# Unit Test
<p>
Unit testing is the process of testing that a particular function returns expected results for different set of inputs.

A unit test is supposed to test standard inputs and corner cases.

A unit test should only test the logic defined inside the tested function.

Most calls to additional functions should be mocked, especially if they make network or database calls.

```The goal of a unit test is to answer the question```: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.</p>

# Execute your tests with

```$ python -m unittest path/to/test_file.py```

# Assertion raises
```
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)
```

# patch

# mock

moc means gives a cover or a modified copy, or "the output i want" for methoods that requires waiting like requests with urls 

# Is it necessary to use mockig with patch or I can use them spereately?
You can use `patch` and `Mock` separately or together, depending on what you need to accomplish. Let's break down the scenarios:

### 1. **Using `patch` Without `Mock`**

`patch` itself is often sufficient when you just want to replace an object or a method with a mock for the duration of your test. In this case, `patch` will automatically create a mock object for you, so you don't need to use `Mock` explicitly.

**Example:**

```python
import unittest
from unittest.mock import patch
from utils import get_json

class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('utils.requests.get') as mock_get:
            # The `patch` automatically creates `mock_get` as a mock object
            mock_get.return_value.json.return_value = test_payload
            
            # Call the function with the test URL
            result = get_json(test_url)
            
            # Assert the get method was called exactly once with the test URL
            mock_get.assert_called_once_with(test_url)
            
            # Assert that the function's output matches the expected payload
            self.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()
```

In this case, `patch` automatically provides a mock object (`mock_get`), so you don't explicitly use `Mock`.

### 2. **Using `Mock` Without `patch`**

You might use `Mock` independently if you want to create mock objects for testing purposes without replacing any existing objects or methods in your code. This is useful when you’re testing interactions with objects that are passed as arguments or returned from functions.

**Example:**

```python
import unittest
from unittest.mock import Mock
from utils import get_json

class TestGetJson(unittest.TestCase):

    def test_custom_mock(self):
        # Create a mock object
        mock_response = Mock()
        mock_response.json.return_value = {"payload": True}
        
        # You can use this mock object directly in your test
        result = mock_response.json()
        
        # Assert that the mock's json method returns the expected value
        self.assertEqual(result, {"payload": True})

if __name__ == '__main__':
    unittest.main()
```

Here, `Mock` is used to create a standalone mock object, and no patching is involved.

### 3. **Using `patch` and `Mock` Together**

As seen in the earlier examples, using `patch` and `Mock` together can give you more control over what the mock returns or how it behaves, especially when you need to configure the mock object in specific ways.

**Summary:**

- **Use `patch` alone** when you just need to replace an existing object or method with a mock.
- **Use `Mock` alone** when you need to create mock objects for testing without replacing anything in your code.
- **Use `patch` and `Mock` together** when you need to replace something and also configure the behavior of the mock object explicitly.

All three approaches are valid and useful in different situations, depending on the complexity and requirements of your tests.


```<a href=https://medium.com/@rohaangurunathrevankar/mocking-for-unit-tests-using-python-5e1fedde4f97> HERE IS A LIBK FOR MAOCK AND PATCH </a>```
