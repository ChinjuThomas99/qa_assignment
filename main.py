import pandas as pd

def findTotalArticlesByLanguages(*languages):
    # URL to the page 
    url = "https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table"
    
    # Read the table data using Pandas
    tables = pd.read_html(url)
    
   # Combine all matching tables into a single DataFrame
    relevant_tables = []
    for table in tables:
        if 'Articles' in table.columns and 'Language' in table.columns:
            relevant_tables.append(table)
    #print(relevant_tables)
            
        # Concatenate all relevant tables into one DataFrame
    if not relevant_tables:
        raise ValueError("No relevant tables found!")
    
    data = pd.concat(relevant_tables, ignore_index=True)

    # Clean and process the table
    pd.set_option('future.no_silent_downcasting', True)
    data['Articles'] = data['Articles'].replace({',': ''}, regex=True).astype(int)  # Convert 'Articles' to int
    
    
    # Normalize the "Language" column to avoid mismatches
    data['Language'] = data['Language'].str.strip().str.lower()
    

    
    # Normalize the input languages for comparison
    languages = [lang.lower() for lang in languages]
    #print(languages)
    
    # Calculate the total articles for the given languages
    total_articles = (data[data['Language'].isin(languages)]['Articles']).sum()
    
    return total_articles

# Example Usage
total = findTotalArticlesByLanguages("English", "German")
print(f"Total articles for the specified languages: {total}")