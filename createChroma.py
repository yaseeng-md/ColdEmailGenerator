from chromadb import PersistentClient
import pandas as pd

class CreateChromaDatabase:
    def __init__(self,csv_path):
        self.csv_path = csv_path
    
    def readCSV(self):
        df = pd.read_csv(self.csv_path)
        return df

    def create_db(self):
        df = self.readCSV()
        client = PersistentClient(path="./chromadb/")
        collection = client.create_collection(name = "yaseeng")
        collection.add(
            documents=df["Technologies"].tolist(),
            metadatas=df[["Project", "Link"]].to_dict(orient="records"),
            ids=[str(i) for i in df.index]
            )
        return collection

if __name__ == "__main__":
    csv_path = "data/yaseen-projects.csv" 
    chroma_db_creator = CreateChromaDatabase(csv_path)
    collection = chroma_db_creator.create_db()
    print("Chroma database created and populated.")