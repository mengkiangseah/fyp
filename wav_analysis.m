filename = 'recording2.wav';

[y,samplingfreq] = audioread(filename);
information = audioinfo(filename);

timing = linspace(0, information.Duration, information.TotalSamples);
%%
figure('position', [0 0 1280 800]);
plot(timing, y);
axis([0, information.Duration, min(y), max(y)]);
xlabel('Time/s')
ylabel('Value')
set(findall(gcf,'type','axes'),'fontsize',50);
set(findall(gcf,'type','text'),'fontSize',50);

%%
begin = 1.5e4;
finish = 1.6e4;

figure('position', [0 0 1280 800]);
plot(timing, y);
axis([1.2, 1.6, min(y), max(y)]);
xlabel('Time/s')
ylabel('Value')
set(findall(gcf,'type','axes'),'fontsize',50);
set(findall(gcf,'type','text'),'fontSize',50);