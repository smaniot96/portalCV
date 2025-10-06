
from django.conf import settings
import os
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(
api_key=os.getenv("GROQ_API_KEY"),
base_url="https://api.groq.com/openai/v1"
)

def generate_cv(data):
    """
    Generate a CV or cover letter based on provided form data.

    Args:
        data (dict): Dictionary with keys like name, email, job_title, etc.
    """
    CV_structure_metadata = r"""
                                \documentclass[10pt, letterpaper]{article}

                                % Packages:
                                \usepackage[
                                    ignoreheadfoot, % set margins without considering header and footer
                                    top=2 cm, % seperation between body and page edge from the top
                                    bottom=2 cm, % seperation between body and page edge from the bottom
                                    left=2 cm, % seperation between body and page edge from the left
                                    right=2 cm, % seperation between body and page edge from the right
                                    footskip=1.0 cm, % seperation between body and footer
                                    % showframe % for debugging 
                                ]{geometry} % for adjusting page geometry
                                \usepackage{titlesec} % for customizing section titles
                                \usepackage{tabularx} % for making tables with fixed width columns
                                \usepackage{array} % tabularx requires this
                                \usepackage[dvipsnames]{xcolor} % for coloring text
                                \definecolor{primaryColor}{RGB}{0, 0, 0} % define primary color
                                \usepackage{enumitem} % for customizing lists
                                \usepackage{fontawesome5} % for using icons
                                \usepackage{amsmath} % for math
                                \usepackage[
                                    pdftitle={Pietro Smaniotto's CV},
                                    pdfauthor={Pietro Smaniotto},
                                    pdfcreator={LaTeX with RenderCV},
                                    colorlinks=true,
                                    urlcolor=primaryColor
                                ]{hyperref} % for links, metadata and bookmarks
                                \usepackage[pscoord]{eso-pic} % for floating text on the page
                                \usepackage{calc} % for calculating lengths
                                \usepackage{bookmark} % for bookmarks
                                \usepackage{lastpage} % for getting the total number of pages
                                \usepackage{changepage} % for one column entries (adjustwidth environment)
                                \usepackage{paracol} % for two and three column entries
                                \usepackage{ifthen} % for conditional statements
                                \usepackage{needspace} % for avoiding page brake right after the section title
                                \usepackage{iftex} % check if engine is pdflatex, xetex or luatex

                                % Ensure that generate pdf is machine readable/ATS parsable:
                                \ifPDFTeX
                                    \input{glyphtounicode}
                                    \pdfgentounicode=1
                                    \usepackage[T1]{fontenc}
                                    \usepackage[utf8]{inputenc}
                                    \usepackage{lmodern}
                                \fi

                                \usepackage{charter}
                                \usepackage{graphicx}
                                % Some settings:
                                \raggedright
                                \AtBeginEnvironment{adjustwidth}{\partopsep0pt} % remove space before adjustwidth environment
                                \pagestyle{empty} % no header or footer
                                \setcounter{secnumdepth}{0} % no section numbering
                                \setlength{\parindent}{0pt} % no indentation
                                \setlength{\topskip}{0pt} % no top skip
                                \setlength{\columnsep}{0.15cm} % set column seperation
                                \pagenumbering{gobble} % no page numbering

                                \titleformat{\section}{\needspace{4\baselineskip}\bfseries\large}{}{0pt}{}[\vspace{1pt}\titlerule]

                                \titlespacing{\section}{-1pt}{0.3cm}{0.2cm}


                                \renewcommand\labelitemi{$\vcenter{\hbox{\small$\bullet$}}$} % custom bullet points
                                \newenvironment{highlights}{
                                    \begin{itemize}[
                                        topsep=0.10 cm,
                                        parsep=0.10 cm,
                                        partopsep=0pt,
                                        itemsep=0pt,
                                        leftmargin=0 cm + 10pt
                                    ]
                                }{
                                    \end{itemize}
                                } % new environment for highlights


                                \newenvironment{highlightsforbulletentries}{
                                    \begin{itemize}[
                                        topsep=0.10 cm,
                                        parsep=0.10 cm,
                                        partopsep=0pt,
                                        itemsep=0pt,
                                        leftmargin=10pt
                                    ]
                                }{
                                    \end{itemize}
                                } % new environment for highlights for bullet entries

                                \newenvironment{onecolentry}{
                                    \begin{adjustwidth}{
                                        0 cm + 0.00001 cm
                                    }{
                                        0 cm + 0.00001 cm
                                    }
                                }{
                                    \end{adjustwidth}
                                } % new environment for one column entries

                                \newenvironment{twocolentry}[2][]{
                                    \onecolentry
                                    \def\secondColumn{#2}
                                    \setcolumnwidth{\fill, 4.5 cm}
                                    \begin{paracol}{2}
                                }{
                                    \switchcolumn \raggedleft \secondColumn
                                    \end{paracol}
                                    \endonecolentry
                                } % new environment for two column entries

                                \newenvironment{threecolentry}[3][]{
                                    \onecolentry
                                    \def\thirdColumn{#3}
                                    \setcolumnwidth{, \fill, 4.5 cm}
                                    \begin{paracol}{3}
                                    {\raggedright #2} \switchcolumn
                                }{
                                    \switchcolumn \raggedleft \thirdColumn
                                    \end{paracol}
                                    \endonecolentry
                                } % new environment for three column entries

                                \newenvironment{header}{
                                    \setlength{\topsep}{0pt}\par\kern\topsep\centering\linespread{1.5}
                                }{
                                    \par\kern\topsep
                                } % new environment for the header

                                \newcommand{\placelastupdatedtext}{% \placetextbox{<horizontal pos>}{<vertical pos>}{<stuff>}
                                \AddToShipoutPictureFG*{% Add <stuff> to current page foreground
                                    \put(
                                        \LenToUnit{\paperwidth-2 cm-0 cm+0.05cm},
                                        \LenToUnit{\paperheight-1.0 cm}
                                    ){\vtop{{\null}\makebox[0pt][c]{
                                        \small\color{gray}\textit{Last updated in September 2024}\hspace{\widthof{Last updated in September 2024}}
                                    }}}%
                                }%
                                }%

                                % save the original href command in a new command:
                                \let\hrefWithoutArrow\href

                    """
    
    CV_begin_document =     r"""
                                \begin{document}
                                \newcommand{\AND}{\unskip
                                    \cleaders\copy\ANDbox\hskip\wd\ANDbox
                                    \ignorespaces
                                }
                                \newsavebox\ANDbox
                                \sbox\ANDbox{$|$}
                            """
    
    CV_structure_header = r"""
                                \begin{header}
                                    \fontsize{25 pt}{25 pt}\selectfont {{GPT:FULL NAME}}\\[6pt]
                                    
                                    \normalsize
                                    \mbox{\hrefWithoutArrow{mailto:{{GPT:EMAIL}}}{{GPT:EMAIL}}} \AND
                                    \mbox{\hrefWithoutArrow{tel:{{GPT:PHONE}}}{Tel: {{GPT:PHONE}}}} \AND
                                    \mbox{\hrefWithoutArrow{{GPT:LINKEDIN_URL}}{Linkedin}} \AND
                                    \mbox{\hrefWithoutArrow{{GPT:GITHUB_URL}}{Github}} \AND
                                    \mbox{\hrefWithoutArrow{{GPT:SCHOLAR_URL}}{Google scholar}}
                                \end{header}
                                
                                \vspace{5 pt - 0.3 cm}

                            """
    
    
    
    CV_section_style = r"""
                                \section{GPT:SECTION_TITLE}
                        """
    CV_section_entry_date = r"""
                                    \begin{twocolentry}{
                                    {{{GPT:DATE_RANGE}}} %use only numbers here in the format XXXX–YYYY
                                }
                                    \textbf{{{{GPT:POSITION_TITLE}}}}, {{{GPT:ORGANIZATION}}}
                                \end{twocolentry}

                                \begin{onecolentry}
                                    \begin{highlights}
                                        \item {{{GPT:HIGHLIGHT_1}}}
                                        \item {{{GPT:HIGHLIGHT_2}}}
                                        %GPT: add more if any
                                    \end{highlights}
                                \end{onecolentry}
                            """
    
    CV_section_entry_no_date = r"""
                                        \begin{onecolentry}
                                        \begin{highlights}
                                            \item {{{GPT:HIGHLIGHT_1}}}
                                            \item {{{GPT:HIGHLIGHT_2}}}
                                            %GPT:add more here if any
                                        \end{highlights}
                                    \end{onecolentry}
                                """
    
    CV_structure_publications = r"""
                                        \begin{samepage}
                                            \begin{twocolentry}{{{{YEAR}}}}
                                                {{{PUBLICATION_TITLE}}}
                                            \end{twocolentry}

                                            \begin{onecolentry}
                                                {{{AUTHORS_AND_LINK}}}
                                            \end{onecolentry}
                                        \end{samepage}
                                """
    
    CV_structure_end_document = r"""
                                \end{document}  
                                """
    # Extract the type first
    generate_type = data.get("Type", "cv")

    # Build the structured prompt automatically
    prompt = f"""
                I want to generate a professional {generate_type.upper()} for the following person.
                I want you to output a latex formatted {generate_type} with the following structure:

                Latex metadata for the CV, you must include all the text provided below before anything else:
                {CV_structure_metadata}
                Then you need to begin document writing the following:
                {CV_begin_document}
                
                Now, given the following data about the person:

                Name: {data.get('name', '')}
                Email: {data.get('email', '')}
                Phone: {data.get('phone', '')}
                LinkedIn: {data.get('linkedin', '')}
                GitHub: {data.get('github', '')}
                Google Scholar: {data.get('google_scholar', '')}
                
                Create header using this template and filling the information where indicated by "GPT:". Include everything in the template provided.
                {CV_structure_header}
                If the info is not provided skip it.
                

                From here you start with the sections using {CV_section_style}

                Four sections follow: Work Experience, Education, Certificates, Languages.

                entries with dates specified will use {CV_section_entry_date} while entries without dates will use {CV_section_entry_no_date}.
                --- Work Experience ---
                {data.get('work_experience', '')}

                --- Education ---
                {data.get('education', '')}

                --- Certificates (Each certificate a two column entry)---
                {data.get('certificates', '')}

                --- Languages ---
                {data.get('languages', '')}

                Last part is publications, if there is no publication skip it.

                --- Publications Data---
                {data.get('publications', '')}
                Structure for publications is:
                {CV_structure_publications}
                
                Now end the document with {CV_structure_end_document} 
                
                Please create a well-formatted, professional {generate_type} with concise language and strong action verbs.
                
                Do not answer with anything other than the CV itself.
                
                Output **pure LaTeX code** only — do not include latex fences or extra text.
                
                Show information only if provided.

                """.strip()

    try:
        chat_completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"❌ Error generating text: {e}"



