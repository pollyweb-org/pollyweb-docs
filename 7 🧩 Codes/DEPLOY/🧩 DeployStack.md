
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>): DeployStack

```yaml
🤝: nlweb.dom/MANIFEST/CODE
Path: /DEPLOY/STACK
Name: Deploy Stack

Schema:
  Version: 1.0

  Properties:
    - Input   # Input parameters for the stack.
    - Params  # Dictionary of parameters for the stack.
    - Include # List of stacks to includ.
    - Deploy  # Dictionary of resources to deploy.

  Format:
    type: object
    properties:

      Input:
        description: Input parameters for the stack.
        type: object
        additionalProperties:
          type: object
          properties:
            
            Optional:
              type: boolean
              default: false
              description: |
                If true, the parameter is optional.
                If false, the parameter is required.

            Default:
              type: string
              description: Default value for the parameter.

      Params:
        description: Dictionary of parameters for the stack.
        type: object
        additionalProperties: true
        properties:

          Handler:
            type: string
            example: BROKER
            description: |
              Default handler for the stack's Lambdas.
                * name of the class to be instanciated.
                * for class X, python will call 'X.Handle{Lambda}()''.

      Include:
        type: array
        items:
          type: string
        description: |
          List of stacks to include.
            * each stack will inherit the parent's parameters.


      deploy:
        description: Dictionary of resources to deploy.
        type: object
        additionalProperties:
          $ref: nlweb.dom/DEPLOY/STACK/RESOURCE
        