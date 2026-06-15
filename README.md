# Open Source Drone

Open Source Drone is a modular quadcopter platform focused on learning aerospace engineering, robotics, and autonomous systems through fully open-source hardware and software.

The project seeks to emphasizes repairability, upgradeability, simulation-driven testing, and transparent documentation throughout development, while also attempting to make access to drones easier and less cost-intensive (hopefully).

## PLEASE NOTE THAT THIS PROJECT IS STILL IN IT'S PILOT PHASE

## THERE WILL BE PLACEHOLDERS

## Repository Structure

## Note that some files are self-explanatory

- drones/drone-versions -> Where you can see more info about the drones
- drones/drone-versions/MK_ (_______) -> Where you can see info about specific drones
- drones/final-steps -> Where you can find the finished product
- drones/final-steps/conclusion.md -> As the name suggests, it's the conclusion
- drones/final-steps/the-finished-drone (N) -> Where you can find the finished drone and it's info
- drones/drone-versions/Requirements.md -> Stuff that should apply to all versions.
- elecronics/MK_ (_______).md -> Where you can see the planned layout of the electronics
- cad/MK_ (_______)/[insert file name here] -> STL files for the drone
- sketches/MK_ (_______)/[insert file name here] -> Sketches and rough drafts can be found here
- calculations/all.md -> Calculations that form the bare minimun
- calculations/MK_ (_______).md -> Specialized calculations, may not be used
- simulations/MK_ (_______).md -> Specialized simulations for the drone

  
## Current Version

MK0 (Bill)

## Version History and Planned Versions

- MK0 (Bill) - Design and Research Prototype, No flight capabilities or electronics planned for this version.
- MK1 (Penguin) - Improved MK0, Will be used for electronics testing, Not planned for flight, Will use rotors producing no lift.
- MK2 (Cicada) - First flight capable model, external mounting points and autonomous capabilities are not planned.
- MK3 (___)
- MK4 (___)
- The Finished Drone (N) - Hopefuly the last drone, might see use as a base, like Bill.

## Goals

- Modular hardware
- Open-source firmware
- Autonomous flight capability
- Computer vision support
- 3D printable components
- Modular payload system
- Obstacle avoidance
- SLAM mapping
- Autonomous mission planning
  
## Current Status

- [x] Research and calculations
- [ ] Frame design
- [ ] Electronics integration
- [ ] Simulation validation
- [ ] Initial flight testing
- [ ] Flight stabilization tuning
- [ ] GPS hold implementation
- [ ] Autonomous navigation
- [ ] Computer vision integration

## Hardware

- 3D printed parts
- COTS electronics (more info to follow)

## Software

- ArduPilot (for autonomous features)
- Mission Planner (for drone control and configuration)
- ExpressLRS (RC link)
- Autodesk Fusion (CAD)
- ProjectAirSim (Testbed)

## Safety

This project is currently in early development and has not yet been flight tested.

Future testing will follow:

- Controlled indoor/isolated outdoor environments
- Pre-flight inspection procedures
- Battery safety protocols
- Propeller safety precautions
- Local drone regulations and airspace rules

## Rule of thumb

This project currently operates on a single active MK design.

All development must reference `design/current_mk_spec.md`.

Other future MK versions are conceptual only and not active.

## Contributing

If you manage to stumble on this project, pull requests, issue reports, and suggestions are welcome.

## License

MIT
