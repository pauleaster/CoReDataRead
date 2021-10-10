from gwpy.timeseries import TimeSeries,TimeSeriesDict


IFOname = ['H1','L1','V1']

H1=TimeSeries(ifos[0].time_domain_strain, sample_rate=sampling_frequency, unit='strain',channel=1,name='H1')
L1=TimeSeries(ifos[1].time_domain_strain, sample_rate=sampling_frequency, unit='strain',channel=1,name='L1')
V1=TimeSeries(ifos[2].time_domain_strain, sample_rate=sampling_frequency, unit='strain',channel=1,name='V1')

H1.write('H1snr288.gwf')
L1.write('L1snr341.gwf')
V1.write('V1snr27.gwf')
