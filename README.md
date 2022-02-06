# Hackathon---Mayu-Checklist-Bot

## Inspiration
The main reason for creating this bot came from seeing friends creating their own google documents to keep track of work, and we wanted to make life easier by making it possible on Discord since most of them use it. 

## What it does
The discord bot code name Mayu takes note of the assignments that students tell the bot to record. Including details such as the name, date, time, and how many people are working on the assignment. The bot will also send out messages and gifs for encouragement and will notify the server when someone is done with an assignment. There are some other hidden cookies if you can find them.

## How we built it
We set up a discord server and used the Discord Developer portal to make our discord bot. Then we used Python and Pycord to code the bot.

## Challenges we ran into
At first, we were mainly struggling with getting commands to work. We tried using events for our commands, but that overcomplicated the entire thing. After a lot of trial and error and problem-solving, we were able to successfully add commands and were moving steadily. In the last 5 or so hours, we were trying to add reminders to our bot, but suddenly our code stopped running. After taking quite a while to figure out the problem, we decided that the time for the reminders weren’t working and we didn’t have time to finish it. In the end, we spent most of our time debugging and learning about new things.

## Accomplishments that we're proud of
Our ability to do research quickly on something we had little knowledge about such as Pycord, and being able to apply that research to actual code. We used the Pycord documentation as well as other sources such as StackOverflow to find the commands and code we needed, which wasn’t always easy due to modules and incompatible code snippets.

## What we learned
We already knew how to code in Python, so coding Discord bots via Pycord was the main concept for us to learn. We learned about using all aspects of the Pycord library, such as event handling with multiple users, inputting commands, having the bot respond to multiple messages in a row, and exception handling. 

## What's next for Mayu Checklist Bot
With the Mayu Bot, our next project is to create a system that will remind the users to accomplish their tasks before the specified due date. This will be done by having the bot directly message them an encouraging message an hour, day, or week before the task is due, sending a higher priority notification that they are more likely to check while keeping the checklist modifiable in the server.
