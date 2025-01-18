<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VeroVi - Advanced Machine Vision Solutions</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/playfair-display/4.7.0/playfair-display.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* :root {
            --primary: #4a0080;
            --secondary: #8a2be2;
            --accent: #b19cd9;
            --dark: #1a0033;
            --light: #f5f0ff;
        } */
        :root {
            --primary: #001B29;
            --secondary: #0A4359;
            --accent: #156C8A;
            --dark: #00131D;
            --light: #F5FAFC;
            --text-light: #FFFFFF;
            --text-dark: #001B29;
        }

        body {
            line-height: 1.6;
            background-color: var(--light);
            font-family: 'Georgia', serif;
            /* color: #333; */
            color: var(--text-dark);
        }

        h1,
        h2,
        h3,
        .logo {
            /* font-family: 'Playfair Display', serif;
            font-weight: 700;
            letter-spacing: -0.02em; */
            display: flex;
            align-items: center;
            height: 60px;
            /* Adjust header height */
        }

        /* Logo image styling */
        .logo img {
            height: 40px;
            /* Adjust based on your preferred logo size */
            width: auto;
            /* Maintain aspect ratio */
            object-fit: contain;
            padding: 0;
            margin: 0;
        }

        p {
            font-size: 1.1rem;
            line-height: 1.8;
        }

        .header {
            /* background: linear-gradient(45deg, var(--primary), var(--secondary)); */
            background: linear-gradient(45deg, #001B29, #0A4359);
            padding: 0.5rem 2rem;
            /* Adjusted padding */
            color: white;
            padding: 1.5rem;
            position: fixed;
            width: 100%;
            z-index: 100;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            height: 100%;
            /* display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto; */
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            /* display: flex;
            gap: 2.5rem; */
            display: flex;
            align-items: center;
            gap: 2.5rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 300;
            font-size: 1.1rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        .hero {
            background: linear-gradient(rgba(0, 27, 41, 0.9), rgba(0, 27, 41, 0.9)),
                /* linear-gradient(rgba(26, 0, 51, 0.9), rgba(26, 0, 51, 0.9)), */
                url('https://d1b5h9psu9yexj.cloudfront.net/57167/DJI-Air-3_20231127-175317_full.jpeg');
            background-size: cover;
            background-position: center;
            /* 50 pixle down the background */
            background-position: 0 50px;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            padding: 0 1rem;
        }

        .hero-content {
            max-width: 900px;
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
        }

        .hero h1 {
            font-size: 4.5rem;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.8rem;
            margin-bottom: 2.5rem;
            font-family: 'Georgia', serif;
            font-weight: 300;
            opacity: 0.9;
        }

        /* .section {
            padding: 7rem 1rem;
            max-width: 1200px;
            margin: 0 auto;
            opacity: 0;
            transform: translateY(20px);
        } */

        
        /* Section Titles */
        .section-title {
            font-size: 3.5rem;
            color: var(--purple);
            text-align: center;
            margin: 3rem auto;
            position: relative;
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            padding-bottom: 1.5rem;
        }

        .section-title::after {
            content: "";
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 3px;
            background: var(--purple-light);
        }

        .section {
            padding: 4rem;
            background-color: var(--purple-bg);
            width: 100%;
        }


        .section.visible {
            animation: slideUp 1s ease-out forwards;
        }

        /* .section-title {
            font-size: 3rem;
            margin-bottom: 4rem;
            text-align: center;
            color: var(--primary);
            position: relative;
        }

        .section-title::after {
            content: "";
            display: block;
            width: 60px;
            height: 3px;
            background: var(--secondary);
            margin: 1rem auto;
        } */
        
        /* .section {
            padding: 7rem 1rem;
            max-width: 1200px;
            margin: 0 auto;
            opacity: 0;
            transform: translateY(20px);
        }

        .section.visible {
            animation: slideUp 1s ease-out forwards;
        }

        .section-title {
            color: #003366;
            font-size: 48px;
            position: relative;
            text-align: center;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 50px;
            height: 2px;
            background-color: #003366;
            position: relative;
            margin: 10px auto 0;
            bottom: -10px;
            left: 0; 
            } 
        */

        .solutions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2.5rem;
        }

        .solution-card {
            background: white;
            padding: 2.5rem;
            border-radius: 0;
            text-align: left;
            transition: transform 0.3s;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .solution-card:hover {
            transform: translateY(-10px);
        }

        .solution-card h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: var(--primary);
        }

        .stats-section {
            background: var(--primary);
            color: white;
            padding: 6rem 1rem;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 3rem;
            text-align: center;
        }

        .stat-card h3 {
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            font-family: 'Playfair Display', serif;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 3rem;
        }

        .team-member {
            text-align: center;
            padding: 3rem;
            background: white;
            border-radius: 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .team-member img {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            margin-bottom: 2rem;
        }

        .team-member h3 {
            font-size: 1.8rem;
            margin-bottom: 0.5rem;
            color: var(--primary);
        }

        .contact-form {
            max-width: 700px;
            margin: 0 auto;
            background: white;
            padding: 3rem;
            border-radius: 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 2rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 0;
            font-family: 'Georgia', serif;
            font-size: 1.1rem;
        }

        .cta-button {
            background-color: var(--secondary);
            color: white;
            padding: 1.2rem 3rem;
            border: none;
            border-radius: 0;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Helvetica Neue', sans-serif;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        .cta-button:hover {
            transform: scale(1.05);
            background-color: var(--primary);
        }

        .footer {
            background: var(--dark);
            color: white;
            padding: 3rem;
            text-align: center;
            font-family: 'Helvetica Neue', sans-serif;
            letter-spacing: 0.05em;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Added Editorial Touches */
        .about-content {
            max-width: 800px;
            margin: 0 auto;
            font-size: 1.2rem;
            line-height: 1.8;
            text-align: justify;
        }

        .quote-section {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            line-height: 1.4;
            text-align: center;
            max-width: 800px;
            margin: 4rem auto;
            color: var(--primary);
            font-style: italic;
        }

        .quote-author {
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 1rem;
            color: #666;
            margin-top: 1rem;
            font-style: normal;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }








        /* Update project section styles */
        .project-container {
            margin: 0;
            padding: 0;
        }

        .project-section {
            min-height: 60vh;
            display: flex;
            align-items: center;
            padding: 6rem 2rem;
            position: relative;
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        .project-content {
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
            display: flex;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        .project-text {
            flex: 0 0 50%;
            padding: 3rem;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .project-section:nth-child(even) .project-content {
            flex-direction: row-reverse;
        }

        .project-title {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1.5rem;
        }

        .project-description {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #333;
        }

        .project-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            /* background: rgba(26, 0, 51, 0.6); */
            background: rgba(0, 27, 41, 0.7);
            z-index: 1;
        }
    </style>

    <!-- <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        :root {
            --primary: #4a0080;
            --secondary: #8a2be2;
            --accent: #b19cd9;
            --dark: #1a0033;
            --light: #f5f0ff;
        }

        body {
            line-height: 1.6;
            background-color: var(--light);
        }

        .header {
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            color: white;
            padding: 1rem;
            position: fixed;
            width: 100%;
            z-index: 100;
        }

        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: 500;
        }

        .hero {
            background: linear-gradient(rgba(26, 0, 51, 0.8), rgba(26, 0, 51, 0.8)), url('/api/placeholder/1200/600');
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            padding: 0 1rem;
        }

        .hero-content {
            max-width: 800px;
            opacity: 0;
            animation: fadeIn 1s ease-out forwards;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }

        .section {
            padding: 5rem 1rem;
            max-width: 1200px;
            margin: 0 auto;
            opacity: 0;
            transform: translateY(20px);
        }

        .section.visible {
            animation: slideUp 1s ease-out forwards;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 3rem;
            text-align: center;
            color: var(--primary);
        }

        .solutions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .solution-card {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .solution-card:hover {
            transform: translateY(-10px);
        }

        .stats-section {
            background: var(--primary);
            color: white;
            padding: 4rem 1rem;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            text-align: center;
        }

        .stat-card h3 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .team-member {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .team-member img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 1rem;
        }

        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .cta-button {
            background-color: var(--secondary);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 5px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: transform 0.3s;
        }

        .cta-button:hover {
            transform: scale(1.05);
            background-color: var(--primary);
        }

        .footer {
            background: var(--dark);
            color: white;
            padding: 2rem;
            text-align: center;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style> -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const sections = document.querySelectorAll('.section');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, { threshold: 0.1 });

            sections.forEach(section => {
                observer.observe(section);
            });
        });
    </script>
</head>

<body>
    <header class="header">
        <nav class="nav">
            <div class="logo"><img src="VeroViLogo2.png" alt="VeroVi logo"></div>
            <div class="nav-links">
                <a href="#solutions">Solutions</a>
                <a href="#about">About</a>
                <a href="#team">Team</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>
    </header>

    <section class="hero">
        <div class="hero-content">
            <h1>Revolutionizing Machine Vision</h1>
            <p>Advanced drone solutions powered by cutting-edge AI technology</p>
            <button class="cta-button">Partner With Us</button>
        </div>
    </section>

    <section id="solutions" class="section">
        <h2 class="section-title">Our Solutions</h2>
        <!-- <div class="solutions-grid">
            <div class="solution-card">
                <h3>Drone Vision Systems</h3>
                <p>State-of-the-art machine vision enabling autonomous drone navigation and advanced aerial imaging
                    capabilities.</p>
            </div>
            <div class="solution-card">
                <h3>Night Vision Recognition</h3>
                <p>Advanced person identification systems operating in low-light conditions with unprecedented accuracy.
                </p>
            </div>
            <div class="solution-card">
                <h3>Tunnel Navigation</h3>
                <p>AI-powered path planning solutions for hazardous and hard-to-reach tunnel environments.</p>
            </div>
            <div class="solution-card">
                <h3>ML Dashboard</h3>
                <p>Comprehensive machine learning monitoring and analytics platform for real-time insights.</p>
            </div>
            <div class="solution-card">
                <h3>Biometric Payments</h3>
                <p>Revolutionary palm print-based payment authentication system for secure transactions.</p>
            </div>
            <div class="solution-card">
                <h3>Custom Solutions</h3>
                <p>Tailored machine vision solutions designed to meet your specific business needs.</p>
            </div>
        </div> -->
    </section>
    <div class="project-container">
        <section class="project-section"
            style="background-image: url('https://cdn1.img.sputniknews.in/img/07e7/0a/05/4614990_0:0:3071:2048_1920x0_80_0_0_a77cca3ba5d7c25ebb5745f1b37b1c7e.jpg.webp')">
            <div class="project-overlay"></div>
            <div class="project-content">
                <div class="project-text">
                    <h2 class="project-title">Drone Vision Systems</h2>
                    <p class="project-description">State-of-the-art machine vision enabling autonomous drone navigation
                        and advanced aerial imaging capabilities.</p>
                </div>
            </div>
        </section>

        <section class="project-section"
            style="background-image: url('https://img.freepik.com/free-photo/people-colorful-thermal-scan-with-celsius-degree-temperature_23-2149170131.jpg')">
            <div class="project-overlay"></div>
            <div class="project-content">
                <div class="project-text">
                    <h2 class="project-title">Night Vision Recognition</h2>
                    <p class="project-description">Advanced person identification systems operating in low-light
                        conditions with unprecedented accuracy.</p>
                </div>
            </div>
        </section>

        <section class="project-section"
            style="background-image: url('https://www.mcelhanney.com/wp-content/uploads/2023/06/MicrosoftTeams-image-42.jpg')">
            <div class="project-overlay"></div>
            <div class="project-content">
                <div class="project-text">
                    <h2 class="project-title">Tunnel Navigation</h2>
                    <p class="project-description">AI-powered path planning solutions for hazardous and hard-to-reach
                        tunnel environments.</p>
                </div>
            </div>
        </section>

        <section class="project-section"
            style="background-image: url('https://sap.github.io/machine-learning-lab/usage/images/exp-ticket-overview.png')">
            <div class="project-overlay"></div>
            <div class="project-content">
                <div class="project-text">
                    <h2 class="project-title">ML Dashboard</h2>
                    <p class="project-description">Comprehensive machine learning monitoring and analytics platform for
                        real-time insights.</p>
                </div>
            </div>
        </section>

        <section class="project-section"
            style="background-image: url('https://dam.mediacorp.sg/image/upload/s--vUQaiCu---/f_auto,q_auto/c_fill,g_auto,h_622,w_830/v1/mediacorp/tdy/image/2023/06/15/20230615_wechat_palm_payment.png?itok=swy2KcNO')">
            <div class="project-overlay"></div>
            <div class="project-content">
                <div class="project-text">
                    <h2 class="project-title">Biometric Payments</h2>
                    <p class="project-description">Revolutionary palm print-based payment authentication system for
                        secure transactions.</p>
                </div>
            </div>
        </section>
    </div>


    <section id="solutions" class="section">
        <h2 class="section-title">Our Stats</h2>
    </section>

    <section class="stats-section section">
        <div class="stats-grid">
            <div class="stat-card">
                <h3>98%</h3>
                <p>Accuracy Rate</p>
            </div>
            <div class="stat-card">
                <h3>50+</h3>
                <p>Enterprise Clients</p>
            </div>
            <div class="stat-card">
                <h3>24/7</h3>
                <p>Technical Support</p>
            </div>
            <div class="stat-card">
                <h3>15+</h3>
                <p>Patents Filed</p>
            </div>
        </div>
    </section>

    <section id="about" class="section">
        <h2 class="section-title">About Us</h2>
        <p style="text-align: center; max-width: 800px; margin: 0 auto;">
            VeroVi is at the forefront of machine vision technology, pioneering innovative solutions that bridge the gap
            between artificial intelligence and real-world applications. Our team of experts combines decades of
            experience in computer vision, drone technology, and artificial intelligence to deliver cutting-edge
            solutions that transform industries.
        </p>
    </section>

    <section id="team" class="section">
        <h2 class="section-title">Our Team</h2>
        <div class="team-grid">
            <div class="team-member">
                <img src="https://media.licdn.com/dms/image/v2/D4D03AQHCeE5pn18LCg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718301870280?e=1742428800&v=beta&t=0UAQdX1Jz41oMDASkpAtILN5yNzxaTBtfilBiEeyUB8"
                    alt="Team Member">
                <h3>Charulkumar</h3>
                <p>Founder</p>
            </div>
            <div class="team-member">
                <img src="https://media.licdn.com/dms/image/v2/D4D03AQGW5eGx-Jp_mQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718217157005?e=1742428800&v=beta&t=RdBWjevtpL8yTTFcNeW6-eIP9KmKVDPebv-2nSan8YU"
                    alt="Team Member">
                <h3>Kinkshuk Gaurav</h3>
                <p>Founder</p>
            </div>
        </div>
    </section>

    <section id="contact" class="section">
        <h2 class="section-title">Contact Us</h2>
        <div class="contact-form">
            <div class="form-group">
                <input type="text" placeholder="Name">
            </div>
            <div class="form-group">
                <input type="email" placeholder="Email">
            </div>
            <div class="form-group">
                <textarea placeholder="Message" rows="5"></textarea>
            </div>
            <button class="cta-button">Send Message</button>
        </div>
    </section>

    <footer class="footer">
        <p>© 2025 VeroVi. Pioneering the Future of Machine Vision.</p>
    </footer>
</body>

</html>
