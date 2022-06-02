
# A cdk template for deploying a merkle proof api for whitelists

a re-deployable template for creating merkle proof apis


Assuming aws cdk has been set up on your machine and `aws configure` has been run

Update `lambda/code/addresses.json` to contain the addresses of the merkle tree


Install lambda dependencies `cd lambda/code/layer/nodejs` and run
```
npm install
```

Return to project root
```
cdk deploy
```
Once deployed you can query the api endpoint with a given address
```
curl https://{{generated api url}}.com/prod/{{address to query}} 
```


