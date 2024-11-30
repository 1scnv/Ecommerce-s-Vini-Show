# Use a imagem oficial do SQL Server
FROM mcr.microsoft.com/mssql/server

# Defina variáveis de ambiente
ENV ACCEPT_EULA=Y
ENV MSSQL_PID=Developer
ENV MSSQL_SA_PASSWORD=123@Mudar
ENV MSSQL_USER=SA

# Exponha a porta 1433
EXPOSE 1433