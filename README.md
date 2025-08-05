# Carbon Countdown

A Flask-based web application that raises awareness about climate change and carbon emissions through an interactive countdown timer and data visualizations.

## 📋 Overview

Carbon Countdown is a three-step educational journey designed to inform users about the climate crisis:

1. **Alarm Phase**: Users encounter a "big scary timer" counting down to 2030, based on UN statements about the critical deadline for reducing carbon emissions by half
2. **Education Phase**: Interactive graphs and data help users understand emission trends across continents and industries
3. **Action Phase**: A curated catalogue of proven organizations where users can contribute to climate solutions

## 🎯 Purpose

The website serves as a symbol and reminder of the climate crisis, emphasizing the urgency to act quickly and effectively. While the countdown shouldn't be taken literally, it represents the critical timeframe we have to make meaningful change.

## 🏗️ Project Structure

```
Carbon_Countdown/
├── templates/           # HTML templates for Flask routes
│   ├── index.html      # Homepage with countdown timer
│   ├── data.html       # Data visualization page ("Why 2030?")
│   ├── help.html       # Action page ("How can I help?")
│   └── about.html      # About page
├── static/
│   └── styles.css      # Custom styling
├── data/
│   ├── analytics.sql   # Database schema for user tracking
│   ├── database/       # Climate data and visualizations
│   │   ├── Yearly_emissions.csv
│   │   ├── climate_data.db
│   │   └── erd.png
│   ├── images/         # Generated chart images
│   └── notebooks/      # Jupyter notebooks for data analysis
├── analytics.db        # SQLite database for user analytics
└── report.pdf         # User tracking analysis report
```

## 🔧 Technical Features

### Web Application
- **Flask Framework**: Python web framework for routing and templating
- **Bootstrap UI**: Responsive design with Bootstrap 5.3.3
- **Interactive Visualizations**: Embedded Plotly charts showing:
  - Continental emission trends (2010-2022)
  - Industry-specific carbon footprints
  - Global emission evolution over time

### Data Analytics
The project includes a custom analytics system that tracks:
- **User Behavior**: Page views, time spent on each page, user flow
- **Technical Metrics**: Load times, browser compatibility, device information
- **Privacy-Focused**: Local SQLite database, no third-party tracking services

### Database Schema
```sql
Users: user_id, ip_address, session_start
Devices: device_id, browser, os
PageViews: pageview_id, user_id, device_id, page, view_time, load_time
```

## 📊 Data Sources

- **Emissions Data**: OECD Quarterly Greenhouse Gas Emissions data
- **Processing**: Jupyter notebooks for data cleaning and transformation
- **Visualization**: Plotly for interactive charts hosted on Plotly's platform

## 🎨 User Experience

### Homepage (index.html)
- Embedded countdown timer from TickCounter
- Contextual video and explanatory text
- Sebastian Vettel climate activism quote
- Clean, card-based layout

### Data Page (data.html)
- Image carousel featuring UN Climate Conference moments
- Interactive Plotly visualizations
- Explanatory text for each data visualization
- Call-to-action directing users to the help page

### Navigation
- Consistent Bootstrap navbar across all pages
- Active page highlighting
- Responsive mobile-friendly design

## 🔍 Analytics Insights

Based on the user tracking report, key improvements were made:
- **Performance**: Switched from local scripting to iframes for better load times
- **Compatibility**: Adjusted tracking code to work with Opera's tracker blockers  
- **Engagement**: Added interactive Plotly graphs and shorter texts to increase user engagement
- **User Flow**: Validated the three-step user journey concept through behavior analysis

## 🛡️ Privacy & Security

### Privacy Considerations
- **Custom Tracking**: Avoids third-party analytics services for better privacy control
- **Minimal Data**: Only collects essential metrics for website improvement
- **Local Storage**: All analytics data stored locally in SQLite database
- **Transparency**: Open source approach allows users to see exactly what data is collected

### Security Notes
- Basic SQLite database (not production-secure)
- No user authentication system
- Static content delivery
- Environment-based configuration recommended for production

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Flask framework
- SQLite3

### Installation
```bash
# Clone the repository
git clone [repository-url]
cd Carbon_Countdown

# Set up virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install flask pandas plotly

# Initialize database
sqlite3 analytics.db < data/analytics.sql

# Run the application
python app.py
```

### Development Notes
- The main `app.py` file appears to be missing from the repository
- Flask session data is stored in the `flask_session/` directory
- Static assets are served from the `static/` directory
- Templates use Jinja2 templating with Bootstrap styling

## 📈 Future Improvements

Based on the tracking analysis report:
- Implement debug mode toggle for analytics
- Add user consent mechanisms for data collection
- Enhance database security for production deployment
- Consider implementing feature flags for A/B testing
- Add automated backup systems for analytics data

## 🌍 Impact

This project demonstrates how data visualization and user experience design can be combined to create awareness about climate change. By making complex emissions data accessible and creating an emotional connection through the countdown timer, it encourages users to take concrete action.

---

*"You can't change what happened. But you can still change what will happen"* - Sebastian Vettel, former F1-driver and climate activist