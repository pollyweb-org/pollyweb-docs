
# [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): DeployStackResource
```yaml
🤝: nlweb.dom/MANIFEST/CODE

Path: /DEPLOY/STACK/RESOURCE
Name: Deploy Stack Resource
 
Schema:
  Version: 1.0

  Properties:
    - Type          # Type of the resource.
    - Dependencies  # List of dependencies for the resource.
    - Params        # Dictionary of parameters for the resource.

  Format:
    type: object
    properties:

      Type:
        description: Type of the resource.
        type: string
        enum:
          
          # Deployment Flow:
          - File          # Reads the content of a file to a string.
          - Python        # Runs Python during the deployment.
          - PostProcessor # Runs Python after the resource is deployed.

          # AWS Resources:
          - Dynamo        # Creates a DynamoDB table.
          - Lambda        # Creates a python Lambda function.
          - Node          # Creates a Node.js lambda from the ./node folder.
          - Parameter     # Creates a parameter in the SSM Parameter Store.
          - Certificate   # Creates an ACM certificate.
          - HostedZone    # Creates a Route53 hosted zone.
          - DnsSecKey     # Creates a Route53 DnsSec key.
          - Secret        # Creates a secret in the Secrets Manager.
          - SnsApp        # Creates an SNS app.
          - SnsTopic      # Creates an SNS topic.
          - SqsQueue      # Creates an SQS queue.
          - RestApi       # Creates a REST API.
          - CloudFront    # Creates a CloudFront distribution.
          - WebAcl        # Creates a WebAcl.

      Dependencies:
        description: List of dependencies for the resource.
        type: array
        items:
          type: string
      
      Params:
        description: Dictionary of parameters for the resource.
        type: object
        additionalProperties: true
        enum: 

          # <any>
          - Trigger     # Dependency that triggers the resource.
          
          # Dynamo
          - Indexes     # Additional global indexes.
          - Stream      # Enable stream on the table.
          - TTL         # Treat TTL as the time-to-live property.
          
          # Lambda
          - Handler     # Handler for the Lambda function.
          - RunAt       # List of times to run the Lambda function.
          - Permissions # List of actions for permissions.
          - Environment # Environment variables for the Lambda function.

          # Parameter
          - Name        # Name of the parameter.

          # Certificate
          - Global      # Create a global certificate instead of Regional.

          # File
          - Path        # Path to the file.

          # SnsApp
          - FirebaseKey # Firebase key for the SNS app.

          # RestApi
          - Handlers    # Dictionary of handlers for the RestApi.

          # WebAcl
          - Global      # Create a global WebAcl instead of Regional.



        properties:
          
          # When Type: *
          # ------------

          Trigger:
            description: |
              Dependency that triggers the resource.
                * Lambda accepts: SQS, SNS, Dynamo
                * SQS accepts: SNS
            type: string


          # When Type: Dynamo
          # ----------------

          Indexes:
            description: Additional global indexes.
            type: array
            items: 
              type: string

          Stream:
            description: Enable stream on the table.
            type: boolean
            default: false

          TTL:
            description: Treat TTL as the time-to-live property.
            type: boolean
            default: false

            
          # When Type: Lambda
          # ----------------

          Handler:
            description: Handler for the Lambda function.
            type: string
            examples: 
              - BROKER
              - BROKER.HandleEvent
              - BROKER.HandleEvent(event, context)

          RunAt:
            description: List of times to run the Lambda function.
            example: [00:00]
            type: array
            items:
              type: string

          Permissions:
            description: List of actions for permissions.
            example: [dynamodb:ListTables]
            type: array
            items:
              type: string

          Environment:
            description: Environment variables for the Lambda function.
            type: object
            additionalProperties: true
            example:
              Param1: Value1
              Param2: Value2
            
        
          # When Type: Parameter
          # -------------------

          Name:
            description: Name of the parameter.
            example: /NLWEB/Config/DomainName
            type: string
            

          # When Type: Certificate, WebAcl
          # ----------------------

          Global:
            description: Create a global resource instead of Regional.
            type: boolean


          # When Type: File
          # ---------------

          Path:
            description: Path to the file.
            type: string
            example: /path/to/file.yaml

          # When Type: SnsApp
          # -----------------

          FirebaseKey:
            description: Firebase key for the SNS app.
            type: string
            example: /path/to/file.yaml

          # When Type: RestApi
          # -----------------

          Handlers:
            description: >
              Dictionary of handlers for the RestApi.
                * key: name of the method, for both GET and POST;
                * value: Lambda dependency.
            type: object
            additionalProperties: 
              type: string
            example: 
              inbox: InboxHandler