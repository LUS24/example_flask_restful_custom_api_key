# Custom decorator for API authorization

This is a simple example of a custom decorator to manage API authorization with an API key.

## Note

- Use python 3.9 or lower.
- Both examples have the same dependencies.

## Endpoints

| Endpoint        | Method | Authorization |
| --------------- | ------ | ------------- |
| /items          |  GET   | None required |
| /item/\<name\>  |  GET   |       JWT     |
| /item/\<name\>  |  POST  | None required |
| /item/\<name\>  |  DEL   |       JWT     |
| /item/\<name\>  |  PUT   | None required |
| /auth           |  POST  | None required |
| /register       |  POST  | None required |
| /store/\<name\> |  POST  |     API Key*  |
| /stores         |  GET   | None required |
| /user/add-device|  POST  |       JWT*    |

*Only after implementing the custom decorator.
