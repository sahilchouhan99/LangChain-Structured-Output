from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

class review(TypedDict):
    Key_themes : Annotated[list[str], "write down all the important theme in this review"]
    summary : Annotated[str, " all brif summary"]
    sentiment : Annotated[str, "give me sentiments positive ,negetive,neutral"]
    pros : Annotated[Optional[list[str]], "pros of the review"]
    cons: Annotated[Optional[list[str]], "cons of the review"]


struture_model=model.with_structured_output(review)

result=struture_model.invoke("""Which mobile do you want a review for? Popular options in 2026 include the Samsung Galaxy S25/S26 series, iPhone 17 series, or Google Pixel 10 series. Let me know the model (or budget/preferences like camera, battery, gaming, etc.) for a tailored review.
Here’s a quick review of the Samsung Galaxy S25 (a strong all-rounder popular in India) based on recent expert tests:
Pros

Compact & Premium Design — Very light and comfortable to hold with slim bezels. Premium build that feels great in hand.
Excellent Display — Bright LTPO OLED (Dynamic AMOLED 2X) with smooth 120Hz refresh rate. Great for media and outdoor use.
Performance — Snapdragon 8 Gen 4 (or equivalent) delivers fast, reliable performance for daily tasks, multitasking, and gaming.
Cameras — Solid all-around system with enhanced AI features for photography and editing. Good low-light and video capabilities.
Battery Life — Competitive endurance with efficient chip and fast charging support. Many users report strong all-day performance.
Software — One UI 7 with useful Galaxy AI tools, excellent customization, and 7 years of OS/security updates.
Value in Segment — Often praised as a balanced flagship without extreme compromises.

Cons

Incremental Upgrades — Not a huge leap from S24 in design or some features — feels evolutionary rather than revolutionary.
Price — Slightly higher than previous generation; premium pricing.
No Major Standouts — Cameras and AI are good but competitors (Pixel for pure photo processing, iPhone for video/ecosystem) may edge it out in specific areas.

Overall Verdict: Excellent choice if you want a compact, reliable Android flagship with great software support and balanced features. Ideal for most users in India who prefer Samsung’s ecosystem, display quality, and after-sales service.""")

print(result)
print(result['summary'])
print(result['sentiment'])