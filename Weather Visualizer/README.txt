# 🌍 Weather Data Visualizer - Python Libraries Project

A beginner-friendly Python project that teaches students how to use external libraries to fetch real-time weather data and create visualizations.

## 🎯 Learning Objectives

By completing this project, students will:
- Understand what libraries are and why we use them
- Learn to make API calls using the `requests` library
- Create data visualizations with `matplotlib`
- Practice working with JSON data structures
- Handle errors gracefully

## 📦 What You'll Need

### Software
- Python 3.7 or higher
- Text editor or IDE (VS Code, PyCharm, IDLE, etc.)
- Internet connection

### Libraries
Install these before starting:
```bash
pip install requests matplotlib
```

### API Key
Get a free API key from OpenWeatherMap:
1. Visit https://openweathermap.org/api
2. Click "Sign Up"
3. Verify your email
4. Copy your API key from the dashboard
5. **Important:** Wait 10-15 minutes for the key to activate!

## 🚀 Getting Started

### Option 1: Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/weather-visualizer.git
cd weather-visualizer
```

### Option 2: Download the starter file
- Download `weather_visualizer_starter.py`
- Save it to your computer
- Open it in your Python editor

### Option 3: Use Google Colab
- Open https://colab.research.google.com/
- Create a new notebook
- Copy the starter code

## 📁 Files in This Repository

```
weather-visualizer/
├── README.md                          # This file!
├── weather_visualizer_starter.py      # Start here (student version)
├── weather_visualizer_solution.py     # Complete solution (teacher reference)
├── data_structures_cheatsheet.md      # Quick reference for Python basics
├── weather_visualizer_lesson.md       # Full lesson plan (teachers)
└── teacher_setup_guide.md             # Setup instructions (teachers)
```

## 📖 How to Use This Project

### For Students:
1. **Read the cheat sheet:** Open `data_structures_cheatsheet.md` for a quick review
2. **Get your API key:** Follow the instructions above
3. **Open the starter file:** Start with `weather_visualizer_starter.py`
4. **Follow the TODOs:** Complete each section marked with `# TODO:`
5. **Run and test:** Test your code frequently as you build
6. **Try extensions:** Once basic version works, try the challenge problems!

### For Teachers:
1. **Read setup guide:** Check `teacher_setup_guide.md` first
2. **Review lesson plan:** See `weather_visualizer_lesson.md` for detailed teaching notes
3. **Test everything:** Run through the project yourself before class
4. **Prepare backups:** Get spare API keys and plan for common issues

## 🎨 What You'll Build

A colorful bar chart that shows current temperatures for cities around the world!

Example output:
```
🌍 Fetching weather data...

✓ London: 18.5°C
✓ Tokyo: 22.0°C
✓ New York: 16.8°C
✓ Sydney: 25.3°C
✓ Dubai: 32.1°C

📊 Successfully fetched data for 5 cities!

[A beautiful bar chart appears!]
```

## 💡 Extension Challenges

Once you have the basic version working, try these:

**Easy:**
- Add 3 more cities to compare
- Change the bar colors
- Modify the chart title

**Medium:**
- Show temperatures in Fahrenheit instead
- Sort cities by temperature (coldest to hottest)
- Add the current date/time to the chart

**Hard:**
- Add a line showing the average temperature
- Create a second chart showing humidity
- Color-code bars based on temperature (blue=cold, red=hot)
- Save the chart as an image file

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'requests'"
**Solution:** Install the library with `pip install requests`

### "Invalid API key"
**Solution:** 
- Make sure you copied the entire key (no spaces)
- Wait 10-15 minutes after signing up
- Check you're using the free API key (not a different product)

### "KeyError: 'main'"
**Solution:**
- City name might be misspelled
- API might be returning an error
- Print the full response to see what you got: `print(data)`

### Chart doesn't display
**Solution:**
- Make sure you called `plt.show()` at the end
- Try running from command line instead of IDE
- Check if `plt.figure()` is called before creating the chart

## 🌟 Example Cities to Try

Try these interesting cities:
- **Hot:** Dubai, Phoenix, Singapore
- **Cold:** Reykjavik, Moscow, Anchorage
- **Unique names:** 
  - Truth or Consequences, US
  - Boring, US
  - Batman, Turkey
  - Why, US

## 📚 Additional Resources

**Learn More:**
- [Requests Documentation](https://requests.readthedocs.io/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/)
- [OpenWeatherMap API Docs](https://openweathermap.org/current)

**Other Free APIs to Try:**
- Cat Facts: https://catfact.ninja/
- Pokemon Data: https://pokeapi.co/
- NASA Images: https://api.nasa.gov/
- Random Quotes: https://api.quotable.io/

## 🤝 Contributing

Found a bug? Have a suggestion? 
- Open an issue on GitHub
- Submit a pull request
- Share your cool visualizations with the class!

## 📄 License

This project is created for educational purposes. Feel free to use and modify for your classes!

## 🙏 Credits

Created for high school students learning Python libraries.

**Built with:**
- [Requests](https://requests.readthedocs.io/) - HTTP library
- [Matplotlib](https://matplotlib.org/) - Visualization library
- [OpenWeatherMap API](https://openweathermap.org/) - Weather data

## 🎉 Share Your Work!

Made something cool? Share it!
- Take a screenshot of your chart
- Push your code to GitHub
- Show your friends and family
- Tag us with #PythonWeatherViz

---

**Questions?** Ask your teacher or check the troubleshooting section above!

**Good luck and have fun! 🚀**