# Paper2Poster: Academic Poster Generator

This project converts academic research papers into visually appealing academic posters using GPT-4o-mini via OpenRouter.

## Generated Posters

Three different poster versions have been created:

1. **Basic Poster** (`poster_output.pptx`): A simple poster with basic formatting
2. **Enhanced Poster** (`enhanced_poster.pptx`): A more visually appealing poster with better layout
3. **Final Poster** (`final_poster.pptx`): A professionally designed poster with color-coded sections and visual elements

## How to Use

### Prerequisites

- Python 3.6+
- OpenRouter API key (set in `.env` file)
- Required Python packages: python-dotenv, openai, pptx, pdf2image, pdfminer.six

### Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install python-dotenv openai python-pptx pdf2image pdfminer.six
   ```
3. Create a `.env` file with your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```

### Generate a Poster

1. Place your research paper PDF in the `dataset/paper/` directory
2. Run one of the following scripts:

#### Basic Poster
```
python simple_poster.py dataset/paper/your_paper.pdf
```

#### Enhanced Poster
```
python extract_full_pptx_text.py  # Extract content from basic poster
python create_enhanced_poster.py  # Create enhanced poster
```

#### Final Poster
```
python create_final_poster.py  # Create final poster with visual enhancements
```

## Script Descriptions

- `simple_poster.py`: Extracts text from PDF and generates a basic poster
- `extract_full_pptx_text.py`: Extracts content from the generated PPTX
- `create_enhanced_poster.py`: Creates an enhanced poster with better layout
- `create_final_poster.py`: Creates a professionally designed poster with visual elements

## Converting to PDF

To convert the PPTX to PDF for viewing:

```
libreoffice --headless --convert-to pdf your_poster.pptx
```

## Notes

- The text extraction process may not capture all content from complex PDFs
- The poster generation is optimized for research papers with standard sections (title, abstract, introduction, methodology, results, conclusion, references)
- You may need to adjust the layout parameters in the scripts for papers with different structures