
The error you’re encountering, `TypeError: '>=' not supported between instances of 'str' and 'datetime.datetime'`, occurs because the comparison you’re attempting to make involves a string data type and a datetime object. To resolve this issue, you need to ensure that the "PublishedDate" column in your dataframe is of the datetime type.

Here’s how you can modify your code to convert the "PublishedDate" column to a datetime format and avoid the TypeError:

1. **Convert the "PublishedDate" column to datetime**:
   Before you start filtering the dataframe based on the date, convert the "PublishedDate" column from a string to a datetime object.

   ```python
   # Convert the 'PublishedDate' column to datetime
   df_prod_metadata['PublishedDate'] = pd.to_datetime(df_prod_metadata['PublishedDate'], errors='coerce')
   ```

2. **Ensure that `past_month` is also a datetime object**:
   If `past_month` is not already a datetime object, convert it as well.

   ```python
   # Assuming past_month is a string, convert it to datetime
   past_month = pd.to_datetime(past_month)
   ```

3. **Filter the dataframe using datetime comparison**:
   Now that both the "PublishedDate" and `past_month` are datetime objects, you can proceed with your filtering.

   ```python
   # Filter the dataframe based on the date
   df_tmp = df_prod_metadata.loc[df_prod_metadata['PublishedDate'] >= past_month]
   ```

With these changes, your code should work correctly, as it will be comparing two datetime objects instead of a string and a datetime object.

Here’s the revised version of your code:

```python
# Convert the 'PublishedDate' column to datetime
df_prod_metadata['PublishedDate'] = pd.to_datetime(df_prod_metadata['PublishedDate'], errors='coerce')

# Assuming past_month is a string, convert it to datetime
past_month = pd.to_datetime(past_month)

# Filter the dataframe based on the date
df_tmp = df_prod_metadata.loc[df_prod_metadata['PublishedDate'] >= past_month]

# The rest of your code remains the same
print(df_tmp.info())

past_month_num_list = []
past_month_perc_list = []

for tag in concept_tags_unique:
    num_with_tag = df_tmp.loc[df_tmp["Concept Tags"].str.contains(tag)].shape[0]
    perc_with_tag = num_with_tag / len(df_tmp)

    past_month_num_list.append(num_with_tag)
    past_month_perc_list.append(str(round(perc_with_tag * 100)) + '%')

output_table_1_df = pd.DataFrame()
output_table_1_df["Concept"] = concept_tags_unique

output_table_1_df["# of Docs this Month"] = past_month_num_list
output_table_1_df["% of Docs this Month"] = past_month_perc_list
```

This should fix the TypeError you’re encountering and allow you to proceed with your analysis.


import setuptools

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project-"
AUTHOR_USER_NAME = "ANSHUL MAHAJAN"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "harshalsharma101@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)