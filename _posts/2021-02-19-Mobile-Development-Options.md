---
title: Explainer - Moble Development Options
date: 2021-02-19 00:00:00 Z
categories:
- daily
tags:
- explainer
layout: post
author: Ted
---

I read a couple of wonderful explainers today on the different methods of app development. Here I will try to summarize to help my understanding.

There are four methods:
1. Native:  Write native code for both iOS and Android.
1. Compiled: Write one codebase that compiles to native code for both iOS and Andriod.
1. Webview Wrappers / Hybrid: One codebase in JavaScript, as with compiled, but it doesn't compile to truly native code. 
1. Progressive Web Apps (PWA): A website that looks like a mobile app and that can be downloaded from the web.

Of course, all have pros and cons:

- Native: The only downside is that you need to write and maintain two code-bases. This is a big downside if you are looking for high speed and low cost. There are many upsides: lots of pre-styled components, full access to the device's hardware, and they have the best performance of the group.
- Compiled: The code reusability is moderate because you are only writing one code-base, but you are not writing "web code". You are writing a codebase that is mapped to and gets compiled down to native iOS and Android code. And the fact that it gets compiled down to native code provides you full access to the device's hardware as a truly native app would. Another downside is the lack of pre-styled components and third-party libraries that you find with all the other options.  
- Hybrid: Here you are writing "web code" that is then packaged up and shipped in an app. It is great to only have to write one codebase in a web-based language like javascript (and this means you can share this code to develop a website too!), but there are a few drawbacks as well. First, the performance is lower than both native and compiled apps (although with the device's big computing power, I am not sure how big of an issue this is nowadays). Secondly, you can't access all of the device's hardware as you can in native and compiled apps.
- PWA: The best way to think about a PWA is that it is just a website that can be downloaded -- so think about the pros and cons of web vs mobile. The web has a very different ecosystem and discovery mechanisms than mobile does. This option has the lowest accessibility to a device's hardware.

In summary, I can see a place and a time for each of the four mobile development options. Over-generalizing: 

- Native for performance and device hardware features.
- Compiled for the same reasons as Native, but with a budget and a timeline.
- Hybrid for development speed: JavaScript, pre-styled components, libraries, and code reusability.
- PWA for super-speed to market, shared code with a website, and web-based distribution.

[Sources #1](https://blog.bitsrc.io/4-ways-to-build-your-mobile-app-make-the-right-choice-efe079c7c817) [Sources #2](https://topflightapps.com/ideas/native-vs-progressive-web-app/)
