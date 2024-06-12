const email = "santiago@athyna.com";
const jobDescription = `About the job
🌏 Context

To drive the successful development of each R&D application, we are looking for a Head of Products. The main missions will be to deliver value to customers and stakeholders, achieve business objectives, advance the company’s competitive position, and nurture collaboration and excellence in product development.

📍 Location

The position is based in one of our offices in Colombia located either in Barranquilla, Bogotá or Cali. Partial remote work is possible, with a regular presence in our office to meet the team.

💼 Missions

Strategic Alignment - Cross-functional Collaboration:
 Ensuring that each product aligns with the overall company strategy and vision.
 Coordinating market research and analysis to understand customer needs, our competitive landscape, and industry trends, and using this information to inform product decisions and strategies, and achieve relevant market positioning.
Product Performance Tracking: Set goals by establishing key performance indicators (KPIs) for each product and regularly monitoring and analyzing metrics to evaluate performance, identify areas for improvement, and use data-driven insights to optimize strategies and resource allocation. 
Cost control: propose budgets, follow-up cost and optimization plans to control/decrease Total Cost of Ownership (TCO). 
Product management global methodology:
 Building Product Management and Quality standards: Set up, promote, and support the implementation of best practices to globally improve our way of making IP-owned software products.
 Iterative Improvement: Fostering a culture of continuous improvement by iterating on product features, gathering feedback from customers, and adapting strategies based on insights and learnings.
Providing leadership, guidance, and mentorship to product managers and cross-functional teams, empowering them to execute on the product vision and achieve success:
 Product Vision: Developing a clear and compelling vision for each product, outlining its purpose, target market, and long-term goals.
 Roadmap Development: Creating and managing a roadmap for each product, prioritizing features and initiatives based on customer needs, market trends, and business objectives. Provide a clear progress status on each product.
 Team alignment: Ensure that the team delivers satisfaction with user-friendly and efficient products that provide value to end-users and clients. Set up their objectives, provide necessary support, and measure performance. Ensure the team has the capacity to ship expected features and to adapt to the changing market environment.
User Experience: Ensuring that each product delivers an exceptional user experience by managing design teams to prioritize usability, accessibility, and aesthetics. 
Revenue Growth: Driving revenue growth for each product through strategic pricing, packaging, and monetization strategies, as well as upsell and cross-sell opportunities. 

🤝 How we work

Driven by the Agile Scrum method, our product teams are organized in squads of 8-9 people featuring a Product Owner, a Lead Developer (acting as Scrum Master), Frontend & Backend Developers and QA Engineers. On top of them, our DevOps Engineers and UI/UX Designers are dedicated to all squads.

🎯 Expected Skills Required

At least 5 years of experience managing a product as a Product Owner and/or a Product Manager with proven track record of managing and launching successful applications. 
At least 2 years of experience in team management whatever the size of the team. 
Communication skills: Excellent verbal and written communication skills will ability to articulate product vision, strategy and roadmap to stakeholders including C-Level. 
Technical proficiency with a good technology background (API, software factory toolset) to understand and support the build process. 
User centric with ability to observe, collect, analyse and transcribe needs into a detailed product specification or user story. 

Nice to have

Experience of management tools such as Jira and Confluence. 
Knowledge of the Customer experience management industry. 

⚙️ Recruitment process

Meet our HR team to ensure alignment between our job offer and your professional project, expectations, mobility, availability, etc. (30 min)
Meet some of our product stakeholders to make sure that you could fit into our existing team. (45 min)
Meet our CTO Nicolas to ensure alignment on business & product visions, and modus operandi. (45 min)`;

(async () => {
  const profile = await fetch(
    "https://extension.api.athyna.com/api/profile/test",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        key: "n7kd3A77kd3H76D)LMTiT6YaDLMiT",
        email,
      }),
    }
  ).then((response) => response.json());

  const promptConfig = {
    jobDescription,
  };

  const profileTailoringPrompt = () => {
    const { tone, jobDescription } = promptConfig;

    let setTone;

    if (tone === 0) setTone = "Make this resume sound professional";
    if (tone === 1) setTone = "Make this resume sound fun";

    const prompt = `
    I want you to act as a hiring manager with 10+ years of experience and help me adapt the resume of a candidate to increase the chances getting hired for a specific job opening.
    Replace words and modify the resume with these key terms from the job description: top, guidance, aesthetics, written, positioning, overall, learnings, building, based, launching, expected, proven, advance, position, featuring, either, control, detailed, nurture, support, possible, backend, acting, propose, landscape, managing, knowledge, designers, clear, lead, tools, confluence, offices, performance, barranquilla, necessary, ability, size, well, optimize, driven, best, customers, job, execute, build, capacity, could, bogotá, promote, driving, opportunities, located, ship, outlining, qa, improve, fit, total, managers, nice, tco, missions, ownership, revenue, people, methodology, success, etc, insights, operandi, aligns, evaluate, excellence, least, kpis, min, looking, understand, tracking, products, main, make, objectives, areas, observe, context, alignment, monetization, factory, hr, presence, coordinating, required, status, value, relevant, competitive, using, allocation, plans, verbal, implementation, delivers, developer, gathering, recruitment, mentorship, identify, mobility, track, offer, regularly, exceptional, purpose, availability, sure, application, clients, dedicated, nicolas, upsell, story, trends, standards, centric, collect, initiatives, whatever, set, iterative, owner, packaging, background, indicators, developing, specification, visions, cto, use, making, adapting, drive, modus, changing, cost, cali, organized, empowering, analyse, partial, providing, excellent, creating, accessibility, one, compelling, adapt, record, transcribe, progress, process, establishing, toolset, frontend, optimization, good, target, devops, needs, deliver, environment, ensure, years, api, monitoring, location, colombia, engineers, r, key, provide, improvement, budgets, globally, measure, resource, existing, articulate, usability, jira, method, squads, proficiency, pricing, achieve, regular, way, iterating, office, culture.
    You can find in separate sections of this prompt the Candidate Resume, the Job Description, and Additional Information with more details on the expected response of your expertise as a hiring manager.
    

  ${tone ? `Tone: ${setTone}` : ""}

    Candidate Resume:
    ----------------------------------------------

    ${profile.firstName} ${profile.lastName}
    ${profile.location ? profile.location : ''}
    ${profile.email ? profile.email : ''}
    ${profile.headline ? profile.headline : ''}

    Professional Summary:
    ${profile.about}

    ${
      profile.workExperience.length > 0
        ? `Work Experience:
          ${profile.workExperience.map((experience) => {
            return `
              ${experience.title} at ${experience.company}
              ${experience.startDate ? experience.startDate : ''} - ${experience.endDate ? experience.endDate : ''}
              ${experience.description ? experience.description : ''}
              `;
          })}
      `
        : ''
    }

    ${
      profile.education.length > 0
        ? `Education:
          ${profile.education.map((education) => {
            return `
              ${education.school}
              ${education.degree ? education.degree : ''}
              ${education.fieldOfStudy ? education.fieldOfStudy : ''}
              ${education.startDate ? education.startDate : ''} - ${education.endDate ? education.endDate : ''}
              `;
          })}`
        : ``
    }

    ${
      profile.skills.length > 0
        ? `Skills:
          ${profile.skills.map((skill) => {
            return `
              ${skill.name}
              `;
          })}`
        : ''
    }

    ${
      profile.licensesAndCertifications.length > 0
        ? `Licenses and Certifications:
          ${profile.licensesAndCertifications.map((license) => {
            return `
              ${license.name}
              `;
          })}
          `
        : ''
    }

    ${
      profile.volunteering.length > 0
        ? `
        Volunteering:
          ${profile.volunteering.map((volunteering) => {
            return `
                  ${volunteering.cause} at ${volunteering.organization}
                  ${volunteering.startDate ? volunteering.startDate : ''} - ${volunteering.endDate ? volunteering.endDate : ''}
                  ${volunteering.description ? volunteering.description : ''}
              `;
          })}
        `
        : ''
    }

    ${
      profile.languages.length > 0
        ? `
        Languages:
        ${profile.languages.map((language) => {
          return `
            ${language.name} - ${language.proficiency ? language.proficiency : ''}
            `;
        })}
    `
        : ''
    }

    Job Description:
    ----------------------------------------------

    ${jobDescription}

    Additional Information:
    ----------------------------------------------

    Use the information of the Job Description Section to adapt and improve the Candidate Resume phrasing and wording, with the objective of increasing the candidate chances of being hired, since the updated resume will resonate more strongly with the job description.

    Use a Professional tone throughout the resume.

    Identify and extract the keywords from the job description to use them in the tailoring.
    
    Translate into english any text on the Candidate Resume that is in a different language for your internal processing of the following instructions.
    
    The new tailored resume MUST show all of the talent work experience. Sort my work experiences in descending order. The most recent work at the beginning.
        
    Absolutely DO NOT make up any information that is not in the resume. If the information is not there, it does not exist and you must leave it as null.
      
    For the skills, use a combination of the ones explicitly mentioned in the resume and the ones mentioned in the job description. If the resume does not mention any skills, use the ones in the job description. Make sure to not have more than 10 skills.
      
    For workExperience and education properties add a new field called bulletPoints, this field is MANDATORY, with bullet points like summary about the description property of each element inside the JSON. Make sure that the bullet points text is not too repetitive with the description because both fields will be visible in the resume. If needed, trim or heavily summary the description itself so the bulletPoints have the main information.
    
    Please ensure that the JSON output adheres strictly to the format provided in the example below. Any deviations from this format are unacceptable. It's crucial that all sections, fields, and structure match exactly as outlined in the example JSON, with all properties being mandatory. Please provide the JSON output as the response, ensuring it follows the specified format without any alterations.
    

    JSON Structure expected for output:
    ----------------------------------------------
    {
      "firstName": "John",
      "lastName": "Doe",
      "location": "San Francisco, CA",
      "headline": "Software Developer",
      "about": "I am a passionate software developer...",
      "workExperience": [
          {
          "title": "Software Developer",
          "company": "Google",
          "startDate": "2019-01-01",
          "endDate": "2021-01-01",
          "description": "I worked on the Google search engine...",
          "bulletPoints": ["Worked in google search engine", "Using high level of programming skills"]
          }
      ],
      "education": [
          {
          "school": "Harvard University",
          "degree": "Bachelor",
          "fieldOfStudy": "Computer Science",
          "startDate": "2015-01-01",
          "endDate": "2019-01-01",
          "description": "I studied computer science at Harvard University...",
          "bulletPoints": ["Studied computer science", "Graduated with honors"]
          }
      ],
      "skills": [
          {
          "name": "JavaScript"
          }
      ],
      "licensesAndCertifications": [
          {
          "name": "AWS Certified Developer"
          }
      ],
      "volunteering": [
          {
          "cause": "Teaching",
          "organization": "Teach for America",
          "startDate": "2018-01-01",
          "endDate": "2020-01-01",
          "description": "I taught computer science to high school students..."
          }
      ],
      "languages": [
          {
          "name": "English",
          "proficiency": "Native"
          }
      ]
    }

    DO NOT SEND IN ANY OTHER FORMAT OR WITH ANY OTHER CHARACTERS LIKE QUOTES OR ANYTHING ELSE. JUST THE JSON OBJECT.
    `;

    return prompt;
  };

  console.log(profileTailoringPrompt());
})();
