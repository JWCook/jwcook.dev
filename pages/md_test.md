# Markdown test
* plain text
* `inline code`
* _italic text_
* **bold text**
  * **_bold italic text_**

## Code blocks

```python
import requests

response = requests.get(
    'https://httpbin.org/get',
    params={'page': '1'},
)
print(response.text)
print(response.headers)
```

```bash
for i in {1..10}; do
    echo "Hello, world $i!"
done
```

## Images
wow look at this cat

![](../assets/images/cat.png)

## Important status update
how else will people know this is a work in progress

oh man this is going to look so cool when it's done

![](../assets/images/underconstruction_2.gif)

![](../assets/images/underconstruction_1.gif) ![](../assets/images/underconstruction_1.gif) ![](../assets/images/underconstruction_1.gif) ![](../assets/images/underconstruction_1.gif) ![](../assets/images/underconstruction_1.gif)