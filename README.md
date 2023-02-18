# simple_parcel_tracker
A simple script that tracks your Lazada parcel shipped by J&amp;T Express PH.

##  What does it do?

*   Opens the [J&T Express Track & Trace webpage][1]
*   Inserts the order number.
*   Lets you see the status of your parcel/order.
*   It uses selenium to open the **Chrome** browser and insert the order number to the input box.

##  How to use it?

*   Open the `main.py` in the `app` folder.
*   Change the `order_number` value with your order number.
*   Run the script with `python3 -m main.py`

*Note: Please ensure you have installed the Chrome browser in your machine*

*Note[2]: The script will attempt to install the chrome webdriver indicated in the code. To change this, please consider editing the following line:*

```Python
# Replace this line:
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# With this line:
PATH = "path/to/your/webdriver.exe"
driver = webdriver.Chrome(PATH)
```

<empty line>

[//]: <> (Author: Jhon Elmer Magloyuan)
[//]: <> (Developer: Jhon Elmer Magloyuan)

[//]: <> (Links)
[1]: https://www.jtexpress.ph/index/query/gzquery.html


