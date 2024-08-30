# PDF_Summarization
PDF SUMMARIZATION USING GEMMA
	Libraries:  Py2PDF, Gemma, Streamlit
	PDF: Data Driven Anomaly

RESULT:


Context: <Read by Py2PDF>
sensors
Article
Data-Driven Anomaly Detection Approach for
Time-Series Streaming Data
Minghu Zhang1,2
, Jianwen Guo1,3,*, Xin Li2,4,5
and Rui Jin1,5
1Key Laboratory of Remote Sensing of Gansu Province, Northwest Institute of Eco-Environment
and Resources, Chinese Academy of Sciences, Lanzhou 730000, China; zhangmh@lzb.ac.cn (M.Z.);
jinrui@lzb.ac.cn (R.J.)
2University of Chinese Academy of Sciences, Beijing 100049, China; xinli@itpcas.ac.cn
3Jiangsu Center for Collaborative Innovation in Geographical Information Resource Development and
Application, Nanjing 210023, China
4National Tibetan Plateau Data Center, Institute of Tibetan Plateau Research, Chinese Academy of Sciences,
Beijing 100101, China
5CAS Center for Excellence in Tibetan Plateau Earth Sciences, Beijing 100101, China
*Correspondence: guojw@lzb.ac.cn
Received: 31 August 2020; Accepted: 28 September 2020; Published: 2 October 2020
/gid00030/gid00035/gid00032/gid00030/gid00038/gid00001/gid00033/gid00042/gid00045 /gid00001
/gid00048/gid00043/gid00031/gid00028/gid00047/gid00032/gid00046
Abstract: Recently, wireless sensor networks (WSNs) have been extensively deployed to monitor
environments. Sensor nodes are susceptible to fault generation due to hardware and software failures
in harsh environments. Anomaly detection for the time-series streaming data of sensor nodes is
a challenging but critical fault diagnosis task, particularly in large-scale WSNs. The data-driven
approach is becoming essential for the goal of improving the reliability and stability of WSNs.
We propose a data-driven anomaly detection approach in this paper, named median ﬁlter (MF)-stacked
long short-term memory-exponentially weighted moving average (LSTM-EWMA), for time-series
status data, including the operating voltage and panel temperature recorded by a sensor node deployed
in the ﬁeld. These status data can be used to diagnose device anomalies. First, a median ﬁlter (MF)
is introduced as a preprocessor to preprocess obvious anomalies in input data. Then, stacked long
short-term memory (LSTM) is employed for prediction. Finally, the exponentially weighted moving
average (EWMA) control chart is employed as a detector for recognizing anomalies. We evaluate the
proposed approach for the panel temperature and operating voltage of time-series streaming data
recorded by wireless node devices deployed in harsh ﬁeld conditions for environmental monitoring.
Extensive experiments were conducted on real time-series status data. The results demonstrate that
compared to other approaches, the MF-stacked LSTM-EWMA approach can signiﬁcantly improve the
detection rate (DR) and false rate (FR). The average DR and FR values with the proposed approach are
95.46% and 4.42%, respectively. MF-stacked LSTM-EWMA anomaly detection also achieves a better
F2score than that achieved by other methods. The proposed approach provides valuable insights
for anomaly detection in WSNs by detecting anomalies in the time-series status data recorded by
wireless sensor nodes.
Keywords: wireless sensor network; environmental monitoring; anomaly detection; fault diagnosis.
data mining
1. Introduction
The in-situ deployment of large numbers of wireless sensor nodes in areas of interest plays an
increasingly important role in the sensing environment owing to recent developments and trends in
wireless sensor networks (WSNs). The WSN enables easy deployment of networked environment
Sensors 2020 ,20, 5646; doi:10.3390 /s20195646 www.mdpi.com /journal /sensors






Response: <SUMMARISED BY GEMMA>
The article provides a comprehensive overview of a data-driven anomaly detection approach for time-series streaming data in WSNs. The key points of the article are as follows:

**Background: **
* WSNs are susceptible to sensor failures due to hardware and software failures.
* Anomaly detection is a critical task for improving the reliability and stability of WSNs.

**Proposed Approach: **
* A median filter (MF) is introduced as a preprocessor to remove obvious anomalies in the input data.
* Stacked long short-term memory (LSTM) is employed for prediction.
* An exponentially weighted moving average (EWMA) control chart is used as a detector for recognizing anomalies.

**Evaluation: **
* The proposed approach is evaluated on real-time time-series status data recorded by wireless node devices deployed in harsh field conditions.
* Extensive experiments are conducted to demonstrate the effectiveness of the proposed approach.

**Key Features: **
* Median filter (MF): Removes obvious anomalies in the input data.
* Stacked LSTM: Predicts future values based on past observations.
* Exponentially weighted moving average (EWMA): Detects anomalies by analyzing the rate of change in the data.
**Results and Discussion: **
* The proposed approach achieves high detection rates and low false alarm rates.
* It provides valuable insights for anomaly detection in WSNs.

**Conclusion: **
* The data-driven anomaly detection approach proposed in the article is effective in detecting anomalies in time-series streaming data in WSNs.
* It provides a valuable tool for improving the reliability and stability of WSNs.

**Keywords: **
* Wireless sensor network; environmental monitoring; anomaly detection; fault diagnosis; data mining

