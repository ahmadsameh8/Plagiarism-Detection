import pandas as pd
import time
import argostranslate.translate
import argparse

def translate_with_api(df, column_name, src_lang='en', dest_lang='ar', delay=5):
    def translate_text(text):
        try:
            translated_text = argostranslate.translate.translate(text, src_lang, dest_lang)
            time.sleep(delay)  # Delay to prevent API throttling
            return translated_text
        except Exception as e:
            print(f"Translation error: {e}")
            return None

    # Apply the translation function to the DataFrame
    df['translated_text'] = df[column_name].apply(translate_text)
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate a CSV column using Argos Translate")
    
    parser.add_argument("file_path", help="Path to the input CSV file")
    parser.add_argument("column_name", help="Column name to translate")
    parser.add_argument("--src_lang", default="en", help="Source language (default: 'en')")
    parser.add_argument("--dest_lang", default="ar", help="Destination language (default: 'ar')")
    parser.add_argument("--output", default="translated_output.csv", help="Output CSV file name (default: translated_output.csv)")
    
    args = parser.parse_args()

    df = pd.read_csv(args.file_path)

    if args.column_name not in df.columns:
        print(f"Error: Column '{args.column_name}' not found in CSV file.")
    else:
        translated_df = translate_with_api(df, args.column_name, args.src_lang, args.dest_lang)
        translated_df.to_csv(args.output, index=False)
        print(f"Translation completed! Output saved to {args.output}")
