
# Step Function Validator (AWS)

An issue we have is that we are quite human and we often make mistakes in the YAML "code". 
These could be syntactical errors (for example, an incorrect indent), but also semantical (for example, forgetting to add a required parameter to a step). 
We only find out about these errors in the last step of the CI/CD, when the step function fails to deploy to AWS. This makes troubleshooting very.. slow...

So we came up with this little tool. 

## Authors

- [@b0tting](https://github.com/b0tting)
- [@NileshDebix](https://github.com/NileshDebix)

