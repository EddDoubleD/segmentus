import kagglehub

# Download latest version
path = kagglehub.dataset_download("manisha717/dataset-of-pdf-files")
print("Path to dataset files:", path)