filename = 'recording3.wav';

[y,samplingfreq] = audioread(filename);
information = audioinfo(filename);

timing = linspace(0, information.Duration, information.TotalSamples);

plot(timing, y);
axis([0, information.Duration, min(y), max(y)]);

%%
begin = 1.5e4;
finish = 1.6e4;

plot(y(1:end));