from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO

from tools.eda_tool import eda_summary
from agents.insight_agent import generate_insights

app = FastAPI(title="CSV Analysis API")

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):

    # 1️⃣ Validate file type
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed."
        )

    try:
        # 2️⃣ Read uploaded file safely
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))

        # 3️⃣ Perform EDA
        eda = eda_summary(df)

        # 4️⃣ Generate AI insights
        insight = generate_insights(df)

        # 5️⃣ Return response
        return {
            "filename": file.filename,
            "rows": df.shape[0],
            "columns": df.shape[1],
            "eda": eda,
            "insight": insight
        }

    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="CSV file is empty.")

    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="Invalid CSV format.")

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing file: {str(e)}"
        )
