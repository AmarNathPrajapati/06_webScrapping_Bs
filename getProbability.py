def calculate_probability(data):
    count_ceo = 0
    count_total = 0

    for entry in data:
      for key, value in entry.items():
          if isinstance(value, str) and "microsoft" in value.lower():
              count_total += 1
              if "ceo" in value.lower() and "amarnath" in value.lower():
                  count_ceo += 1
    if count_total == 0:
        return 0  # Return 0 if there are no mentions of Fourbrick in the data

    probability = count_ceo / count_total
    return probability

# Given data
data= [
    {
      "Heading 1": "Amarnath Venkat - Microsoft",
      "Description 1": "Working as a BigData Engineer in MICROSOFT, Hyderabad | Learn more about Amarnath Venkat's work experience, education, connections & more by visiting their ...Working as a BigData Engineer in MICROSOFT, Hyderabad | Learn more about Amarnath Venkat's work experience, education, connections & more by visiting their ...",
      "Heading 2": "Amarnath P C - Manager - Microsoft",
      "Description 2": "Amarnath P C · Support Engineering Manager · View mutual connections with Amarnath · Welcome back · Activity · Experience · Education · Licenses & ...Amarnath P C · Support Engineering Manager · View mutual connections with Amarnath · Welcome back · Activity · Experience · Education · Licenses & ...",
      "Heading 3": "Amarnath - Microsoft Apps",
      "Description 3": "7 Jan 2024 — Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.7 Jan 2024 — 7 Jan 2024Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.",
      "Heading 4": "Amarnath - Microsoft এপ্‌সমূহ",
      "Description 4": "7 Jan 2024 — Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.7 Jan 2024 — 7 Jan 2024Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.",
      "Heading 5": "Amarnath - Microsoft ആപ്പുകൾ",
      "Description 5": "7 Jan 2024 — Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.7 Jan 2024 — 7 Jan 2024Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.",
      "Heading 6": "Amarnath - Microsoft ಆಪ್‌ಗಳು",
      "Description 6": "7 Jan 2024 — Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.7 Jan 2024 — 7 Jan 2024Amarnath is a 1978 Indian Kannada film, directed by K. Mani Murugan and produced by N. K. Narayan, V. K. Ramesh and P. B. Walke.",
      "Heading 7": "Amarnath V Microsoft Excel No reviews yet",
      "Description 7": "Hi, my name is Amarnath. I am an ex-student of IIT Roorkee. I developed an interest in MS Excel during my college days. Then after graduation I decided to ...Hi, my name is Amarnath. I am an ex-student of IIT Roorkee. I developed an interest in MS Excel during my college days. Then after graduation I decided to ...",
      "Heading 8": "AMARNATH BGDR Impossible Screen Guard for ...",
      "Description 8": "Buy AMARNATH BGDR Impossible Screen Guard for MICROSOFT LUMIA 535 DUAL_SIM only for Rs. from Flipkart.com. Only Genuine Products.Buy AMARNATH BGDR Impossible Screen Guard for MICROSOFT LUMIA 535 DUAL_SIM only for Rs. from Flipkart.com. Only Genuine Products.",
      "Heading 9": "Amarnath Sikdar helped me reinstall Microsoft Office 365. ...",
      "Description 9": "20 Aug 2019 — Amarnath Sikdar helped me reinstall Microsoft Office 365. My computer is working fine. He did a good job. - Answered by a verified Microsoft ...20 Aug 2019 — 20 Aug 2019Amarnath Sikdar helped me reinstall Microsoft Office 365. My computer is working fine. He did a good job. - Answered by a verified Microsoft ...",
      "Heading 10": "Amarnath gupta an educationist and mentor | PPT",
      "Description 10": "15 Sept 2013 — Dr. Amarnath Gupta is an educationist, author, and founder of Integrated Management Consultants. He has over 9 years of experience serving ...15 Sept 2013 — 15 Sept 2013Dr. Amarnath Gupta is an educationist, author, and founder of Integrated Management Consultants. He has over 9 years of experience serving ..."
    },
    {
      "Heading 1": "Amarnath Singh - Founder & CEO - Vision Trade India ...",
      "Description 1": "Amar Nath Singh, Founder & CEO, Visiontrade India Innovation Pvt Ltd always says, \"We ensure to connect every business within India or abroad with its new ...Amar Nath Singh, Founder & CEO, Visiontrade India Innovation Pvt Ltd always says, \"We ensure to connect every business within India or abroad with its new ...",
      "Heading 3": "Amarnath Halember - NextG Apex India Pvt Ltd",
      "Description 3": "I am the CEO and founder of NextG Apex India Pvt Ltd, a company that specializes in… · Experience: NextG Apex India Pvt Ltd · Education: Young Scientists ...I am the CEO and founder of NextG Apex India Pvt Ltd, a company that specializes in… · Experience: NextG Apex India Pvt Ltd · Education: Young Scientists ...",
      "Heading 4": "Amarnath Yatra: Shrine board CEO conducts extensive ...",
      "Description 4": "17 Jun 2023 — The chief executive officer (CEO) of the Shri Amarnath Shrine Board (SASB), Dr Mandeep Bhandari on Friday conducted a comprehensive tour of ...17 Jun 2023 — 17 Jun 2023The chief executive officer (CEO) of the Shri Amarnath Shrine Board (SASB), Dr Mandeep Bhandari on Friday conducted a comprehensive tour of ...",
      "Heading 5": "CEO Shri Amarnath Ji Shrine Board Reviews Yatra ...",
      "Description 5": "JAMMU : Principal Secretary to Lieutenant Governor and Chief Executive Officer Shri Amarnath Ji Shrine Board, Mandeep K. Bhandari on Monday chaired a.JAMMU : Principal Secretary to Lieutenant Governor and Chief Executive Officer Shri Amarnath Ji Shrine Board, Mandeep K. Bhandari on Monday chaired a.",
      "Heading 6": "Amarnath Singh - Founder & CEO @ VISIONTRADE INDIA",
      "Description 6": "Amarnath Singh is the Founder and CEO of VISIONTRADE INDIA.Amarnath Singh is the Founder and CEO of VISIONTRADE INDIA.",
      "Heading 7": "Shri Amarnath Ji Shrine Board.",
      "Description 7": "Hon'ble Lieutenant Governor, UT of J&K is the Chairman of the Shrine Board.. The Shrine Board is responsible for better management of the Shri Amarnathji Yatra, ...Hon'ble Lieutenant Governor, UT of J&K is the Chairman of the Shrine Board.. The Shrine Board is responsible for better management of the Shri Amarnathji Yatra, ...",
      "Heading 8": "Amar Nath Gupta, Premier Explosives Ltd",
      "Description 8": "Amar Nath Gupta is Former Chairman/Managing Dir/Founder at Premier Explosives Ltd. See Amar Nath Gupta's compensation, career history, education, & memberships ...Amar Nath Gupta is Former Chairman/Managing Dir/Founder at Premier Explosives Ltd. See Amar Nath Gupta's compensation, career history, education, & memberships ...",
      "Heading 9": "Shri Amarnath Ji Yatra 2023 | CEO SASB conducts ...",
      "Description 9": "16 Jun 2023 — He emphasised the importance of timely completion of all necessary arrangements to facilitate a safe and comfortable Yatra experience for the ...16 Jun 2023 — 16 Jun 2023",
      "Heading 11": "Principal secretary to Jammu and Kashmir LG and SASB ...",
      "Description 11": "8 May 2023 — Dr Mandeep K Bhandari, the principal secretary to the lieutenant governor and chief executive officer of the Shri Amarnath Ji Shrine Board (SASB) ...8 May 2023 — 8 May 2023Dr Mandeep K Bhandari, the principal secretary to the lieutenant governor and chief executive officer of the Shri Amarnath Ji Shrine Board (SASB) ..."
    },
    {
      "Heading 2": "Satya Nadella",
      "Description 2": "Satya Narayana Nadella is an Indian-American business executive. He is the executive chairman and CEO of Microsoft, succeeding Steve Ballmer in 2014 as CEO ...Satya Narayana Nadella is an Indian-American business executive. He is the executive chairman and CEO of Microsoft, succeeding Steve Ballmer in 2014 as CEO ...",
      "Heading 3": "Satya Nadella - Microsoft",
      "Description 3": "Satya Nadella Satya Nadella is an influencer. Microsoft The University of Chicago Booth School of Business. Redmond, Washington, United States.Satya Nadella Satya Nadella is an influencer. Microsoft The University of Chicago Booth School of Business. Redmond, Washington, United States.",
      "Heading 7": "Who is Satya Nadella, Family, Salary, Education, Net Worth ...",
      "Description 7": "Satya Narayana Nadella is the chief executive officer (CEO) of Microsoft. Under him, Microsoft has more cloud computing revenue than Google, more subscribers ...Satya Narayana Nadella is the chief executive officer (CEO) of Microsoft. Under him, Microsoft has more cloud computing revenue than Google, more subscribers ...",
      "Heading 8": "Satya Nadella (@satyanadella) / X",
      "Description 8": "Chairman and CEO at Microsoft.Chairman and CEO at Microsoft.",
      "Heading 9": "Microsoft chairman and CEO Satya Nadella highlights ...",
      "Description 9": "7 Feb 2024 — Microsoft chairman and CEO Satya Nadella highlights opportunity for an AI-empowered India to accelerate inclusive growth and development.7 Feb 2024 — 7 Feb 2024Microsoft chairman and CEO Satya Nadella highlights opportunity for an AI-empowered India to accelerate inclusive growth and development.",
      "Heading 10": "Satya Nadella | Biography & Facts",
      "Description 10": "17 Jan 2024 — On February 4, 2014, Nadella became CEO of Microsoft, the third person to hold the office in the company's nearly 40-year history, after company ...17 Jan 2024 — 17 Jan 2024On February 4, 2014, Nadella became CEO of Microsoft, the third person to hold the office in the company's nearly 40-year history, after company ..."
    },
    {
      "Heading 1": "Avinash Amarnath - Microsoft",
      "Description 1": "Deepak Avinash Amarnath. Founder & CEO : DABB. Chennai. Avinash Amarnath. Hyderabad. Avinash Amarnath. Technical lead - Mechanical. Madurai. 5 others named ...Deepak Avinash Amarnath. Founder & CEO : DABB. Chennai. Avinash Amarnath. Hyderabad. Avinash Amarnath. Technical lead - Mechanical. Madurai. 5 others named ...",
      "Heading 2": "Amarnath Ch - Microsoft",
      "Description 2": "“Amarnath was one of the key members of our development team. He is a competent developer, pays close attention to detail and learns new tasks quickly. He is a ...“Amarnath was one of the key members of our development team. He is a competent developer, pays close attention to detail and learns new tasks quickly. He is a ...",
      "Heading 3": "Rishab Amarnath | CEO at Compass Career Discoverers",
      "Description 3": "View Rishab Amarnath's profile on F6S - Compass Career Discoverers - The assessment center model that we have built for students is one which was made ...View Rishab Amarnath's profile on F6S - Compass Career Discoverers - The assessment center model that we have built for students is one which was made ...",
      "Heading 4": "A Amarnath Reddy, IEG CEO on Engineering Education",
      "Description 4": "22 Jul 2011 — Empathy- My Success Secret - Satya Nadella, Microsoft CEO · Innovative ecosystem is key for entrepreneurship · View all. Latest. Join the AP ...22 Jul 2011 — 22 Jul 2011Empathy- My Success Secret - Satya Nadella, Microsoft CEO · Innovative ecosystem is key for entrepreneurship · View all. Latest. Join the AP ...",
      "Heading 5": "Software Engineer - Amarnath Chakala's email & phone",
      "Description 5": "8 May 2023 — ... microsoft.com & phone: + ... Amarnath Chakala's email address is cxx@news.microsoft ... The Chairman & CEO of the Microsoft is Satya Nadella.8 May 2023 — 8 May 2023... microsoft.com & phone: + ... Amarnath Chakala's email address is cxx@news.microsoft ... The Chairman & CEO of the Microsoft is Satya Nadella.",
      "Heading 6": "IEEE SIGHT Founder Amarnath Raja Dies at 65",
      "Description 6": "23 Nov 2022 — Amarnath Raja. Founder of IEEE Special Interest Group on Humanitarian Technology. Senior member, 65; died 5 September.23 Nov 2022 — 23 Nov 2022Amarnath Raja. Founder of IEEE Special Interest Group on Humanitarian Technology. Senior member, 65; died 5 September.",
      "Heading 8": "Amarnath Reddy email address & phone number",
      "Description 8": "Amarnath Reddy, based in Hyderabad, Telangana, India, is currently a Technical Lead at Amnet Digital, bringing experience from previous roles at Wipro ...Amarnath Reddy, based in Hyderabad, Telangana, India, is currently a Technical Lead at Amnet Digital, bringing experience from previous roles at Wipro ...",
      "Heading 9": "Amarnath S, Author at Tech Blogs by TechAffinity - Page 2 ...",
      "Description 9": "Amarnath is a techno functional person from Pre-Sales Team. And keen on keeping himself updated on new technologies. He has around 3+ Year's Experience in ...Amarnath is a techno functional person from Pre-Sales Team. And keen on keeping himself updated on new technologies. He has around 3+ Year's Experience in ...",
      "Heading 10": "Amarnath Yatra resumes on Pahalgam route after 3 days ...",
      "Description 10": "10 Jul 2023 — The Amarnath Yatra has resumed after being suspended for ... Amarnath Yatra resumes on Pahalgam ... CEO quits high-paying Microsoft job in US to ...10 Jul 2023 — 10 Jul 2023The Amarnath Yatra has resumed after being suspended for ... Amarnath Yatra resumes on Pahalgam ... CEO quits high-paying Microsoft job in US to ..."
    }
  ]
# Calculate probability
probability = calculate_probability(data)
print("Probability that Sundar Pichai is the CEO of google:", probability)
