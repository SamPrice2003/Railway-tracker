# Railway Tracker – Problem Definition

## Background and Motivation

Rail travel in the UK is widely perceived as unreliable, with frequent delays, cancellations, and service disruptions. Passengers regularly experience overcrowded trains, unclear communication, and limited visibility into how severe or systemic these issues actually are. While frustration is common, there is little accessible, data-driven evidence that quantifies rail performance in a clear and comparable way.

Although national rail operators expose large volumes of data through public APIs, this data is fragmented, technically complex, and difficult to interpret without specialist knowledge. As a result, it is hard for passengers, researchers, and analysts to objectively answer basic questions about rail reliability.



## Problem Definition

There is no simple, unified system that aggregates publicly available rail data and turns it into clear, comparable performance metrics.

Specifically, it is difficult to:
- Quantify how often trains are cancelled or delayed
- Measure the severity of delays in a consistent way
- Compare rail performance across stations, regions, and time periods
- Understand whether poor service reflects isolated incidents or wider systemic issues
- Receive timely, relevant alerts about disruptions affecting specific journeys

This lack of transparency makes it hard to move beyond anecdotal complaints and towards evidence-based understanding of rail performance.



## Project Objective

The objective of the Railway Tracker project is to build a data driven platform that transforms complex rail data into clear, measurable insight. The system aims to quantify delays and cancellations, surface trends over time, and communicate this information through dashboards, reports, and notifications.

The focus of the project is descriptive and analytical: measuring what has happened and what is currently happening, rather than predicting future performance or influencing rail operations.



## Proposed Solution

The Railway Tracker will:
- Ingest historical and near real-time rail data from public APIs
- Normalise and store this data for short-term and aggregated analysis
- Calculate performance metrics over rolling time windows
- Monitor live incidents and service disruptions
- Expose insights through user-facing dashboards, reports, and alerts

The system is designed to separate data ingestion, storage, analysis, and presentation, allowing each part to evolve independently while remaining aligned to the core problem.



## Core Metrics

For a selected set of stations in the north and south of England, the system will calculate:
- Percentage of trains cancelled in the last 24 hours
- Percentage of trains delayed by more than 5 minutes
- Average delay across all trains
- Average delay across trains delayed by more than 1 minute
- Summary of service incidents and disruption reasons



## Real-Time Monitoring and Notifications

In addition to historical analysis, the system will monitor real-time disruption and incident feeds. Users will be able to subscribe to notifications for specific stations or lines and receive alerts via email or SMS when relevant incidents occur.

The goal is to provide timely, targeted information rather than constant, low-value notifications.



## Data Sources and Constraints

The project will use:
- National Rail APIs (Darwin feed)

These data sources present several constraints:
- Data is event-based rather than relational
- Reference data is separated from live operational data
- Schemas vary across providers
- Access to live feeds may be limited or require streaming connections

The system is designed to work within these constraints, with clear documentation of data limitations and appropriate use of fallback or simulated data where necessary.



## Planned Outputs

The primary user-facing outputs are:
- An interactive dashboard showing delay and cancellation metrics, trends, and comparisons
- Automated daily summary reports stored in object storage and emailed to subscribers
- Real-time email or SMS alerts for disruptions affecting selected stations or lines



## Definition of Success

The project will be considered successful if it:
- Produces clear and defensible delay and cancellation metrics
- Helps users understand how rail performance varies across time and location
- Communicates complex data in a way that is accessible to non-technical users
- Provides a solid foundation for future extensions or deeper analysis



## Initial User Stories

As a rail passenger, I want to see how often trains at my local station are delayed or cancelled so that I can understand how reliable the service actually is.

As a user, I want to compare rail performance between different stations or regions so that I can see whether delays are isolated or systemic.

As a subscriber, I want to receive email or SMS alerts for disruptions on specific stations or lines so that I can react to issues affecting my journey.

As an analyst, I want access to clear, standardised delay and cancellation metrics so that I can explore trends and patterns over time.



## Summary

Railway Tracker aims to move the discussion of UK rail reliability from anecdote to evidence. By aggregating fragmented rail data, calculating meaningful performance metrics, and presenting them clearly, the project provides a shared, data-driven understanding of how well the rail network is actually performing.