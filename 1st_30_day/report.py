from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Enhanced content for the slides
slides_content = [
    {
        "title": "DNA Replication",
        "content": "DNA Replication is the biological process by which a cell makes an exact copy of its DNA. This is essential for cell division and inheritance, ensuring that each daughter cell receives a complete set of genetic instructions."
    },
    {
        "title": "What is DNA Replication?",
        "content": ("DNA replication is the process of duplicating a DNA molecule. It ensures that each new cell has the same genetic information. "
                    "This occurs in the nucleus of eukaryotic cells during the S phase of Interphase before the cell enters mitosis or meiosis. "
                    "Replication is vital for growth, repair, and reproduction in organisms.")
    },
    {
        "title": "How Does DNA Replication Begin?",
        "content": ("Replication begins at specific locations called Origins of Replication. At these sites, the DNA unwinds, creating a structure "
                    "known as the Replication Fork. This Y-shaped region is where new DNA strands are synthesized. Multiple origins allow replication to occur rapidly in eukaryotes.")
    },
    {
        "title": "Enzymes Involved in DNA Replication",
        "content": ("1. Helicase: Unzips the DNA double helix by breaking hydrogen bonds.\n"
                    "2. DNA Polymerase: Adds new complementary nucleotides to each original strand.\n"
                    "3. Ligase: Joins fragments of DNA and seals any breaks in the sugar-phosphate backbone.")
    },
    {
        "title": "Step 1: Helicase Action",
        "content": "Helicase binds to the DNA at the origin and separates the two strands by breaking the hydrogen bonds between the base pairs, forming the replication fork."
    },
    {
        "title": "Step 2: Primer Addition",
        "content": ("RNA Primase adds short RNA primers on both DNA strands. These primers are necessary starting points for DNA Polymerase to begin nucleotide addition. "
                    "Primers are later removed and replaced with DNA.")
    },
    {
        "title": "Step 2: DNA Polymerase Activity",
        "content": ("DNA Polymerase reads the existing DNA strands and adds complementary nucleotides (A with T, G with C). "
                    "This enzyme works continuously on the leading strand and in short fragments on the lagging strand.")
    },
    {
        "title": "Step 3: Okazaki Fragments",
        "content": ("Because DNA Polymerase can only add nucleotides in one direction (5’ to 3’), the lagging strand is synthesized in short, discontinuous segments called Okazaki fragments. "
                    "These fragments are later joined to form a continuous strand.")
    },
    {
        "title": "Step 4: Ligase Seals DNA",
        "content": ("DNA Ligase joins the Okazaki fragments and seals nicks in the sugar-phosphate backbone, resulting in two continuous DNA strands. "
                    "This completes the process of replication.")
    },
    {
        "title": "Result of Replication",
        "content": "The result is two identical DNA molecules. Each molecule consists of one original strand and one newly synthesized strand—ensuring genetic consistency across generations."
    },
    {
        "title": "Semi-conservative Model",
        "content": ("Watson and Crick proposed that DNA replication is semi-conservative. This means each new DNA molecule retains one strand from the parent molecule and includes one newly synthesized strand, "
                    "providing both accuracy and a template for the next replication.")
    },
    {
        "title": "Mutations During Replication",
        "content": ("Mutations are errors in DNA replication where the base sequence is altered. Although DNA Polymerase proofreads and corrects most errors, some slip through. "
                    "External factors like UV light, chemicals, and radiation can also cause mutations, potentially leading to genetic disorders or cancer.")
    }
]

# Create a new detailed PDF
enhanced_pdf_path = "/mnt/data/enhanced_dna_replication.pdf"
c = canvas.Canvas(enhanced_pdf_path, pagesize=letter)
width, height = letter

for slide in slides_content:
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 100, slide["title"])
    c.setFont("Helvetica", 12)
    text_object = c.beginText(50, height - 150)
    text_object.setLeading(16)
    for line in slide["content"].split("\n"):
        text_object.textLine(line)
    c.drawText(text_object)
    c.showPage()

c.save()
enhanced_pdf_path
