<html>

<head>
    <meta>charset="utf-8"</meta>
    <meta>http-equiv = "X-UA-Compatible" content="IE=edge"</meta>
    <meta>name="view-port" content="width=device-width, initial-scale=1.0"</meta>
    <script type="text/javascript" src="./productManager.js"></script>
    <link rel="stylesheet" href="./pm.css" />
    <title>Product Manager</title>
</head>
<body>
    <form action="">
    <div name="data" class="productManager">
        <h1>Product Manager</h1>
        
        <label for="idNumber">ID</label>
        <input type="text" id="idNumber" class="inputID"></input>

        <label for="description">Description</label>
        <input type="text" id="description" class="inputDescription"></input>
        
        <label for="unitaryPrice">Unitary Price</label>
        <span class="currency">$ </span>
        <input type="text" id="unitaryPrice" name="amount" class="inputUnitaryPrice" length = "15"></input>

        <label for="state">State</label>
        <select name="state" id="state" class="selectState">
            <option value="available">Available</option>
            <option value="notAvailable">Not Available</option>
        </select>
    </div>  
    <div name="crudButtons" class="buttonManager">
        <button>Search</button>
        <button>Create</button>
        <button>Update</button>
        <button>Delete</button>
    </div>
    <div name="listData" class="listManager">
        <table style="width:100%">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Description</th>
                    <th>Unit Price</th>
                    <th>State</th>
                </tr>
            </thead>
            <tbody>
                <tr> th:each="Product Manager: $ {listData}"
                 <td th:text="${Object.id}">Product ID</td>
                 <td th:text="${Object.description}">Description</td>
                 <td th:text="${Object.unitPrice}">Unit Price</td>
                 <td th:text="${Object.state}">State</td>
                </tr>
            </tbody>
        </table>
    </div>
  </form>
</body>
</html>