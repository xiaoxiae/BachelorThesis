# Thesis

- [Clis](https://github.com/Climber-Tools/Clis) – efficient 3D scanning of climbing holds and climbing gym interiors.
- [Cled](https://github.com/Climber-Tools/Cled) – a 3D editor designed for efficient virtual routesetting.

## Abstract
With the rising popularity of sport climbing and bouldering, there are increasing incentives to take it to the online space.
This thesis does so in way suitable for regular climbing gyms.
A workflow for creating 3D hold and wall models and the accompanying editor has been developed, so that routes can be copied from the real world to the virtual one and be interacted with in a more immersive way.

## Introduction
With the rising popularity of climbing and bouldering, in no small part due to the addition of the sport to the Tokyo 2020 Summer Olympics, climbing gyms are seeing a steady increase in new climbers.
An obvious attraction to both climbers and route setters is being able to virtually view the current way the holds are set up (the current "setting"). This offers a great number of advantages, such as:

-   archiving older settings for tracking trends like difficulty and style,
-   saving an existing route to be rebuilt later (useful in competitions),
-   being able to view the current setting online before visiting a gym and seeing if it is suitable (and possibly opting to go somewhere else if not),
-   filtering boulders by difficulty and popularity,
-   setting community-made boulders (if an editor exists) and
-   adding a social aspect by (dis)liking and commenting on boulders, adding videos and beta[^1] hints, connecting with other climbers, etc.

Models of boulders are gradually becoming used in competitive climbing and certain gyms, lead mainly by the OnlineObservation team.
Their approach is simple -- take photos of the wall with the holds already on it and use them to generate a 3D model.
This works really well for a one-time model generation, but becomes infeasible for a climbing gym that replaces boulders periodically, as the model would have to be regenerated each time, which takes a significant amount of time and specialized equipment for higher quality models.
It is also difficult to individually highlight certain boulders and edit them if a change is made after the modelling.

This thesis attempts to solve the problem by focusing on what actually changes from setting to setting -- the position of the holds on the wall.
The repeated scanning of the holds and the wall adds redundancy, which could be removed by a program that edits the placements of the holds.
This adds time initially, since models of the wall and the holds have to be created.
However, it saves time after repeated settings and offers the aforementioned advantages, making it a viable option for commercial climbing gyms.

A system for semi-automatic scanning of climbing holds has been developed to efficiently create hold models, along with a workflow for modelling climbing wall interiors ([Clis – the climber's scanner](https://github.com/Climber-Tools/Clis)).
The generated data is then used in a virtual editor that can be used to efficiently model the routes ([Cled – the climber's editor](https://github.com/Climber-Tools/Cled)).

The process and techniques behind the creation of the hold and wall models are described in section 1.
The functionality and implementation of the editor are covered in section 2.
Appendices A and B provide a quickstart for the scanning and editing, respectively.

## Building
1. Type `make`.
2. Press `enter`.
3. Profit?

## License
Parts of the code (esp. the title page) are based on the original template (available from the faculty website) by Martin Mareš, Arnošt Komárek, and Michal Kulich.

University and faculty logos are a property of the respective universities and faculties.

Everything else is licensed under GPLv3.

[^1]: A term used for the intended sequence of moves for reaching the
    top of the route.
