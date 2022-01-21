# Market api

## Use terms:

    Project made by Priccila, for a technical test, only use this for fun and not to earn money

### How to init:

### Routes:

    Post /user:

    {
    "nick_name": "str",
    "email": "xxxx@xxxx.com",
    "password": "str"
    }
    Response:201,

    {
        "id": 556,
        "nick_name": "user12_name",
        "email": "emaailaa@email.com"
    }


    Post /login
    {
        "email": "str",
        "password": str
    }
    Response: 200
    {
        "TOKEN": "str"
    }


    Delete /user/id
        Header: Authorization Bearer token

        Response: 204


    Patch /user/id
        Header: Authorization Bearer token
        {
            "nick_name": str
        }
        Response: 202
        {
            "nick_name": str
        }


    Get /products

    Response: 200
    [
        {
            "id": "str",
            "name": "str",
            "price", float -> in pennies
        }
    ]


    Get /products/id

    response: 200
    [
        {
            {
            "id": "str",
            "name": "str",
            "price": float,
            "promotions": [
                    {
                      "id": "str",
                      "type": "str",
                      "required_qty int,
                      "free_qty int
                    }]
            }
        }
    ]


    Post /products
    [
        {
          "id": "4MB7UfpTQs",
          "name": "Boring Fries!",
          "price": 199,
        	"quantity": 1,
          "promotions": []
        },
    	{
        "id": "Dwt5F7KAhi",
        "name": "Amazing Pizza!",
        	"quantity": 3,
        "price": 1099,
        "promotions": [
          {
            "id": "ibt3EEYczW",
            "type": "QTY_BASED_PRICE_OVERRIDE",
            "required_qty": 2,
            "price": 1799
          }
        ]
    },

        	{
          "id": "PWWe3w1SDU",
          "name": "Amazing Burger!",
          "price": 999,
        	"quantity": 2,
          "promotions": [
            {
              "id": "ZRAwbsO2qM",
              "type": "BUY_X_GET_Y_FREE",
              "required_qty": 2,
              "free_qty": 1
            }
          ]
        },
        	{
          "id": "C8GDyLrHJb",
        	"quantity": 1,
          "name": "Amazing Salad!",
          "price": 499,
          "promotions": [
            {
              "id": "Gm1piPn7Fg",
              "type": "FLAT_PERCENT",
              "amount": 10
            }
          ]
        }
        ]

        Response: 200
        {
          "total price": float,
          "total disccount": float,
          "total spent": float
        }
